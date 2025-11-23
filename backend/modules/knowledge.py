"""
Knowledge Base Module - RAG Local
=================================
Indexa archivos markdown y permite búsqueda semántica usando embeddings.

Stack:
- sentence-transformers (all-MiniLM-L6-v2) para embeddings
- ChromaDB para almacenamiento vectorial
"""

from pathlib import Path
from typing import Optional
from loguru import logger
import re

try:
    from sentence_transformers import SentenceTransformer
    import chromadb
    from chromadb.config import Settings
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False
    logger.warning("Dependencias de Knowledge Base no instaladas")


class KnowledgeBase:
    """
    Knowledge Base con búsqueda semántica.

    Uso:
        kb = KnowledgeBase(data_dir="./data/vectors")
        kb.index_folder("/path/to/markdown/files")
        results = kb.search("¿cómo funciona RAG?")
    """

    # Modelo de embeddings (ligero y rápido)
    MODEL_NAME = "all-MiniLM-L6-v2"
    COLLECTION_NAME = "directos_knowledge"

    def __init__(self, data_dir: Path):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.model = None
        self.client = None
        self.collection = None

        if DEPS_AVAILABLE:
            self._initialize()

    def _initialize(self):
        """Inicializar modelo y base de datos"""
        try:
            logger.info(f"Cargando modelo de embeddings: {self.MODEL_NAME}")
            self.model = SentenceTransformer(self.MODEL_NAME)

            logger.info(f"Inicializando ChromaDB en: {self.data_dir}")
            self.client = chromadb.PersistentClient(
                path=str(self.data_dir),
                settings=Settings(anonymized_telemetry=False)
            )

            self.collection = self.client.get_or_create_collection(
                name=self.COLLECTION_NAME,
                metadata={"hnsw:space": "cosine"}
            )

            logger.info(f"Knowledge Base inicializada. Documentos: {self.collection.count()}")

        except Exception as e:
            logger.error(f"Error inicializando Knowledge Base: {e}")
            self.model = None

    def is_ready(self) -> bool:
        """Verificar si el módulo está listo"""
        return self.model is not None and self.collection is not None

    def _chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
        """
        Dividir texto en chunks para mejor indexación.

        Args:
            text: Texto completo
            chunk_size: Tamaño aproximado de cada chunk (caracteres)
            overlap: Solapamiento entre chunks

        Returns:
            Lista de chunks
        """
        # Dividir por párrafos primero
        paragraphs = re.split(r'\n\n+', text)

        chunks = []
        current_chunk = ""

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def index_file(self, file_path: Path) -> int:
        """
        Indexar un archivo markdown.

        Returns:
            Número de chunks indexados
        """
        if not self.is_ready():
            return 0

        file_path = Path(file_path)
        if not file_path.exists() or file_path.suffix not in ['.md', '.txt']:
            return 0

        try:
            text = file_path.read_text(encoding='utf-8')
            chunks = self._chunk_text(text)

            if not chunks:
                return 0

            # Generar embeddings
            embeddings = self.model.encode(chunks).tolist()

            # Preparar datos para ChromaDB
            ids = [f"{file_path.stem}_{i}" for i in range(len(chunks))]
            metadatas = [{"source": str(file_path), "chunk": i} for i in range(len(chunks))]

            # Añadir a la colección
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=chunks,
                metadatas=metadatas
            )

            logger.info(f"Indexado: {file_path.name} ({len(chunks)} chunks)")
            return len(chunks)

        except Exception as e:
            logger.error(f"Error indexando {file_path}: {e}")
            return 0

    def index_folder(self, folder_path: str, patterns: list[str] = None) -> int:
        """
        Indexar todos los archivos markdown de una carpeta.

        Args:
            folder_path: Ruta a la carpeta
            patterns: Patrones de archivos a incluir (default: *.md)

        Returns:
            Total de chunks indexados
        """
        if not self.is_ready():
            return 0

        folder = Path(folder_path)
        if not folder.exists():
            logger.warning(f"Carpeta no existe: {folder_path}")
            return 0

        patterns = patterns or ["*.md", "*.txt"]
        total = 0

        for pattern in patterns:
            for file_path in folder.rglob(pattern):
                # Ignorar archivos ocultos y node_modules
                if any(part.startswith('.') for part in file_path.parts):
                    continue
                if 'node_modules' in file_path.parts:
                    continue

                total += self.index_file(file_path)

        logger.info(f"Indexación completada: {total} chunks de {folder_path}")
        return total

    def search(self, query: str, limit: int = 5) -> list[dict]:
        """
        Búsqueda semántica.

        Args:
            query: Texto de búsqueda
            limit: Número máximo de resultados

        Returns:
            Lista de resultados con text, source, score
        """
        if not self.is_ready():
            return []

        try:
            # Generar embedding de la query
            query_embedding = self.model.encode([query]).tolist()

            # Buscar en ChromaDB
            results = self.collection.query(
                query_embeddings=query_embedding,
                n_results=limit,
                include=["documents", "metadatas", "distances"]
            )

            # Formatear resultados
            formatted = []
            for i, doc in enumerate(results['documents'][0]):
                formatted.append({
                    "text": doc,
                    "source": results['metadatas'][0][i].get('source', 'unknown'),
                    "score": 1 - results['distances'][0][i]  # Convertir distancia a similitud
                })

            return formatted

        except Exception as e:
            logger.error(f"Error en búsqueda: {e}")
            return []

    def get_stats(self) -> dict:
        """Obtener estadísticas de la knowledge base"""
        if not self.is_ready():
            return {"ready": False, "count": 0}

        return {
            "ready": True,
            "count": self.collection.count(),
            "model": self.MODEL_NAME,
            "path": str(self.data_dir)
        }

    def clear(self):
        """Limpiar toda la knowledge base"""
        if self.client and self.collection:
            self.client.delete_collection(self.COLLECTION_NAME)
            self.collection = self.client.get_or_create_collection(
                name=self.COLLECTION_NAME,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info("Knowledge Base limpiada")
