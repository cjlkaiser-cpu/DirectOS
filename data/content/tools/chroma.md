---
id: chroma
name: ChromaDB
category: Storage
icon: fa-database
color: text-emerald-400
tag: Vector DB
status: used
level: solid
next: ChromaDB clustering
---

# ChromaDB

Base de datos para guardar vectores (embeddings).

## Por qué en minerOS

Es donde vive la 'memoria semántica' de minerOS. Permite buscar por significado ('algo parecido a esto') en lugar de palabras exactas.

## Casos de uso

- Motor de búsqueda RAG
- Recomendaciones
- Memoria de chatbot

## Código ejemplo

```python
collection = client.get_collection('fotos')
results = collection.query(query_texts=['atardecer'], n_results=5)
```

## Proyectos que lo usan

- DirectOS v6.0 (Knowledge Base RAG)
- PhotoMine v1.4 (búsqueda semántica visual)
