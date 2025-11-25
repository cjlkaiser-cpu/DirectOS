"""
Content Manager - Lee archivos Markdown con frontmatter
=======================================================
Módulo para cargar herramientas, patrones, flows desde archivos .md

Stack:
- python-frontmatter para parsear YAML frontmatter
- Cache en memoria para performance
"""

from pathlib import Path
from typing import Optional, List, Dict
from loguru import logger
import frontmatter


class ContentManager:
    """
    Gestiona contenido en archivos Markdown.

    Uso:
        cm = ContentManager(base_dir="./data/content")
        tools = cm.get_tools()
        tool = cm.get_tool("clip")
    """

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self._cache: Dict[str, List[Dict]] = {}
        logger.info(f"ContentManager inicializado en: {self.base_dir}")

    def _load_markdown_file(self, file_path: Path) -> Optional[Dict]:
        """
        Lee un archivo .md con frontmatter y devuelve un dict.

        Returns:
            {
                "id": "clip",
                "name": "OpenAI CLIP",
                ...metadatos del frontmatter...,
                "content": "# OpenAI CLIP\n\nModelo multimodal..."
            }
        """
        try:
            post = frontmatter.load(file_path)

            # Combinar metadatos + contenido
            data = dict(post.metadata)
            data['content'] = post.content
            data['file'] = str(file_path)

            return data

        except Exception as e:
            logger.error(f"Error leyendo {file_path}: {e}")
            return None

    def _load_category(self, category: str) -> List[Dict]:
        """
        Carga todos los archivos .md de una categoría.

        Args:
            category: "tools", "patterns", "flows", "presets"

        Returns:
            Lista de dicts con los datos parseados
        """
        category_dir = self.base_dir / category

        if not category_dir.exists():
            logger.warning(f"Categoría no existe: {category_dir}")
            return []

        items = []
        for md_file in category_dir.glob("*.md"):
            data = self._load_markdown_file(md_file)
            if data:
                items.append(data)

        logger.info(f"Cargados {len(items)} items de '{category}'")
        return items

    def get_tools(self, reload: bool = False) -> List[Dict]:
        """
        Obtiene todas las herramientas.

        Args:
            reload: Si True, recarga desde disco (ignora cache)

        Returns:
            Lista de herramientas como dicts
        """
        if reload or 'tools' not in self._cache:
            self._cache['tools'] = self._load_category('tools')

        return self._cache['tools']

    def get_tool(self, tool_id: str) -> Optional[Dict]:
        """
        Obtiene una herramienta específica por ID.

        Args:
            tool_id: ID de la herramienta (ej: "clip")

        Returns:
            Dict con la herramienta o None si no existe
        """
        tools = self.get_tools()
        for tool in tools:
            if tool.get('id') == tool_id:
                return tool
        return None

    def get_patterns(self, reload: bool = False) -> List[Dict]:
        """Obtiene todos los patrones"""
        if reload or 'patterns' not in self._cache:
            self._cache['patterns'] = self._load_category('patterns')
        return self._cache['patterns']

    def get_flows(self, reload: bool = False) -> List[Dict]:
        """Obtiene todos los flows"""
        if reload or 'flows' not in self._cache:
            self._cache['flows'] = self._load_category('flows')
        return self._cache['flows']

    def get_presets(self, reload: bool = False) -> List[Dict]:
        """Obtiene todos los presets"""
        if reload or 'presets' not in self._cache:
            self._cache['presets'] = self._load_category('presets')
        return self._cache['presets']

    def get_projects(self, reload: bool = False) -> List[Dict]:
        """Obtiene todos los proyectos documentados"""
        if reload or 'projects' not in self._cache:
            self._cache['projects'] = self._load_category('projects')
        return self._cache['projects']

    def get_project(self, project_id: str) -> Optional[Dict]:
        """
        Obtiene un proyecto específico por ID.

        Args:
            project_id: ID del proyecto (ej: "farmaia")

        Returns:
            Dict con el proyecto o None si no existe
        """
        projects = self.get_projects()
        for project in projects:
            if project.get('id') == project_id:
                return project
        return None

    def refresh_cache(self):
        """Limpia y recarga todo el cache"""
        logger.info("Refrescando cache de contenido")
        self._cache = {}
        self.get_tools(reload=True)
        self.get_patterns(reload=True)
        self.get_flows(reload=True)
        self.get_presets(reload=True)
        self.get_projects(reload=True)

    def get_stats(self) -> Dict:
        """Estadísticas del contenido"""
        return {
            "tools": len(self.get_tools()),
            "patterns": len(self.get_patterns()),
            "flows": len(self.get_flows()),
            "presets": len(self.get_presets()),
            "projects": len(self.get_projects()),
            "base_dir": str(self.base_dir)
        }
