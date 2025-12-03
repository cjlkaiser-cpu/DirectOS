"""
Pipeline Executor - DirectOS v9.0 Agent Mode
=============================================
Ejecuta pipelines diseñados en el canvas como código real.

Arquitectura:
1. Recibe definición de pipeline (nodos + conexiones)
2. Construye grafo de ejecución
3. Ejecuta cada nodo en orden topológico
4. Captura output y errores
5. Notifica progreso

Ejemplo de pipeline:
{
    "nodes": [
        {"id": "n1", "tool": "python", "config": {"script": "process.py"}},
        {"id": "n2", "tool": "sqlite", "config": {"db": "data.db"}}
    ],
    "connections": [
        {"from": "n1", "to": "n2"}
    ]
}
"""

import subprocess
import asyncio
import json
import time
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from loguru import logger


class NodeStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    SKIPPED = "skipped"


@dataclass
class ExecutionNode:
    """Nodo de ejecución con estado y resultado"""
    id: str
    tool: str
    config: Dict = field(default_factory=dict)
    status: NodeStatus = NodeStatus.PENDING
    output: str = ""
    error: str = ""
    started_at: float = 0
    finished_at: float = 0

    @property
    def duration(self) -> float:
        if self.finished_at and self.started_at:
            return self.finished_at - self.started_at
        return 0


@dataclass
class PipelineRun:
    """Representa una ejecución de pipeline"""
    id: str
    pipeline_name: str
    nodes: List[ExecutionNode]
    status: str = "pending"  # pending, running, success, error, cancelled
    started_at: float = 0
    finished_at: float = 0
    current_node: str = ""
    progress: int = 0  # 0-100

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "pipeline_name": self.pipeline_name,
            "status": self.status,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "current_node": self.current_node,
            "progress": self.progress,
            "duration": self.finished_at - self.started_at if self.finished_at else 0,
            "nodes": [
                {
                    "id": n.id,
                    "tool": n.tool,
                    "status": n.status.value,
                    "output": n.output[-500:] if n.output else "",  # Últimos 500 chars
                    "error": n.error,
                    "duration": n.duration
                }
                for n in self.nodes
            ]
        }


class PipelineExecutor:
    """
    Motor de ejecución de pipelines.

    Uso:
        executor = PipelineExecutor(work_dir="/tmp/directos")
        run_id = await executor.execute(pipeline_def, on_progress=callback)
        status = executor.get_run(run_id)
    """

    # Mapeo de herramientas a comandos
    TOOL_COMMANDS = {
        "python": "python3 {script}",
        "nodejs": "node {script}",
        "bash": "bash {script}",
        "sqlite": "sqlite3 {db} < {script}",
        "ffmpeg": "ffmpeg {args}",
        "whisper": "whisper {input} --model {model} --output_dir {output}",
        "ollama": "ollama run {model} '{prompt}'",
    }

    def __init__(self, work_dir: Path = None):
        self.work_dir = Path(work_dir) if work_dir else Path.home() / ".directos" / "runs"
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.runs: Dict[str, PipelineRun] = {}
        self.active_processes: Dict[str, subprocess.Popen] = {}
        logger.info(f"PipelineExecutor inicializado en {self.work_dir}")

    def _build_execution_order(self, nodes: List[Dict], connections: List[Dict]) -> List[str]:
        """
        Ordena nodos topológicamente según conexiones.
        Retorna lista de IDs en orden de ejecución.
        """
        # Construir grafo de dependencias
        deps = {n["id"]: set() for n in nodes}
        for conn in connections:
            if conn["to"] in deps:
                deps[conn["to"]].add(conn["from"])

        # Ordenamiento topológico (Kahn's algorithm)
        order = []
        ready = [nid for nid, d in deps.items() if not d]

        while ready:
            node_id = ready.pop(0)
            order.append(node_id)

            for nid, d in deps.items():
                if node_id in d:
                    d.remove(node_id)
                    if not d and nid not in order:
                        ready.append(nid)

        # Si hay nodos sin procesar, hay ciclo
        if len(order) != len(nodes):
            logger.warning("Ciclo detectado en pipeline, usando orden original")
            return [n["id"] for n in nodes]

        return order

    def _build_command(self, tool: str, config: Dict, run_dir: Path) -> Optional[str]:
        """Construye comando ejecutable para un tool"""
        template = self.TOOL_COMMANDS.get(tool)
        if not template:
            # Tool genérico - buscar script o comando en config
            if "command" in config:
                return config["command"]
            if "script" in config:
                return f"python3 {config['script']}"
            return None

        try:
            # Sustituir variables
            cmd = template.format(**config)
            return cmd
        except KeyError as e:
            logger.error(f"Config incompleta para {tool}: falta {e}")
            return None

    async def execute(
        self,
        pipeline_def: Dict,
        on_progress: Callable[[PipelineRun], None] = None,
        on_complete: Callable[[PipelineRun], None] = None
    ) -> str:
        """
        Ejecuta un pipeline de forma asíncrona.

        Args:
            pipeline_def: Definición del pipeline (nodes, connections)
            on_progress: Callback para progreso
            on_complete: Callback al terminar

        Returns:
            run_id: ID de la ejecución
        """
        run_id = f"run_{int(time.time())}_{uuid.uuid4().hex[:6]}"
        run_dir = self.work_dir / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        nodes_def = pipeline_def.get("nodes", [])
        connections = pipeline_def.get("connections", [])

        # Crear nodos de ejecución
        exec_nodes = [
            ExecutionNode(
                id=n["id"],
                tool=n.get("tool", "python"),
                config=n.get("config", {})
            )
            for n in nodes_def
        ]

        # Crear run
        run = PipelineRun(
            id=run_id,
            pipeline_name=pipeline_def.get("name", "Unnamed Pipeline"),
            nodes=exec_nodes
        )
        self.runs[run_id] = run

        # Guardar definición
        (run_dir / "pipeline.json").write_text(json.dumps(pipeline_def, indent=2))

        # Ejecutar en background
        asyncio.create_task(self._execute_pipeline(run, run_dir, on_progress, on_complete))

        logger.info(f"Pipeline iniciado: {run_id} con {len(exec_nodes)} nodos")
        return run_id

    async def _execute_pipeline(
        self,
        run: PipelineRun,
        run_dir: Path,
        on_progress: Callable,
        on_complete: Callable
    ):
        """Ejecuta el pipeline secuencialmente"""
        run.status = "running"
        run.started_at = time.time()

        nodes_by_id = {n.id: n for n in run.nodes}

        # Ordenar ejecución
        nodes_def = [{"id": n.id, "tool": n.tool, "config": n.config} for n in run.nodes]
        order = self._build_execution_order(nodes_def, [])  # TODO: pasar connections

        total = len(order)
        completed = 0

        try:
            for node_id in order:
                node = nodes_by_id.get(node_id)
                if not node:
                    continue

                run.current_node = node_id
                node.status = NodeStatus.RUNNING
                node.started_at = time.time()

                if on_progress:
                    on_progress(run)

                # Construir y ejecutar comando
                cmd = self._build_command(node.tool, node.config, run_dir)

                if cmd:
                    try:
                        # Ejecutar proceso
                        process = await asyncio.create_subprocess_shell(
                            cmd,
                            stdout=asyncio.subprocess.PIPE,
                            stderr=asyncio.subprocess.PIPE,
                            cwd=str(run_dir)
                        )

                        stdout, stderr = await asyncio.wait_for(
                            process.communicate(),
                            timeout=300  # 5 min timeout por nodo
                        )

                        node.output = stdout.decode() if stdout else ""
                        node.error = stderr.decode() if stderr else ""

                        if process.returncode == 0:
                            node.status = NodeStatus.SUCCESS
                        else:
                            node.status = NodeStatus.ERROR
                            logger.error(f"Nodo {node_id} falló: {node.error}")

                    except asyncio.TimeoutError:
                        node.status = NodeStatus.ERROR
                        node.error = "Timeout: proceso excedió 5 minutos"
                    except Exception as e:
                        node.status = NodeStatus.ERROR
                        node.error = str(e)
                else:
                    # Sin comando, simular éxito (nodo de visualización)
                    node.status = NodeStatus.SUCCESS
                    node.output = f"[{node.tool}] Nodo sin comando ejecutable"

                node.finished_at = time.time()
                completed += 1
                run.progress = int((completed / total) * 100)

                # Guardar output
                (run_dir / f"{node_id}.log").write_text(
                    f"=== {node.tool} ===\n{node.output}\n\n=== ERRORS ===\n{node.error}"
                )

                if on_progress:
                    on_progress(run)

                # Si hay error, decidir si continuar o parar
                if node.status == NodeStatus.ERROR:
                    # Por ahora, continuar con otros nodos
                    pass

            # Determinar estado final
            errors = [n for n in run.nodes if n.status == NodeStatus.ERROR]
            run.status = "error" if errors else "success"

        except Exception as e:
            logger.exception(f"Error ejecutando pipeline {run.id}")
            run.status = "error"

        run.finished_at = time.time()
        run.current_node = ""

        # Guardar resultado
        (run_dir / "result.json").write_text(json.dumps(run.to_dict(), indent=2))

        if on_complete:
            on_complete(run)

        logger.info(f"Pipeline {run.id} completado: {run.status}")

    def get_run(self, run_id: str) -> Optional[Dict]:
        """Obtiene estado de una ejecución"""
        run = self.runs.get(run_id)
        return run.to_dict() if run else None

    def get_runs(self, limit: int = 10) -> List[Dict]:
        """Lista ejecuciones recientes"""
        runs = sorted(
            self.runs.values(),
            key=lambda r: r.started_at,
            reverse=True
        )[:limit]
        return [r.to_dict() for r in runs]

    def cancel_run(self, run_id: str) -> bool:
        """Cancela una ejecución en progreso"""
        run = self.runs.get(run_id)
        if not run or run.status != "running":
            return False

        run.status = "cancelled"
        run.finished_at = time.time()

        # TODO: Matar procesos activos
        logger.info(f"Pipeline {run_id} cancelado")
        return True

    def cleanup_old_runs(self, max_age_hours: int = 24):
        """Limpia ejecuciones antiguas"""
        cutoff = time.time() - (max_age_hours * 3600)
        to_remove = []

        for run_id, run in self.runs.items():
            if run.finished_at and run.finished_at < cutoff:
                to_remove.append(run_id)

        for run_id in to_remove:
            del self.runs[run_id]
            run_dir = self.work_dir / run_id
            if run_dir.exists():
                import shutil
                shutil.rmtree(run_dir, ignore_errors=True)

        if to_remove:
            logger.info(f"Limpiadas {len(to_remove)} ejecuciones antiguas")
