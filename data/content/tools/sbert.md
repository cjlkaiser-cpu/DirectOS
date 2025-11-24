---
id: sbert
name: Sentence-BERT
category: IA Model
icon: fa-brain
color: text-teal-400
tag: Embeddings
status: used
level: solid
next: Custom embeddings training
---

# Sentence-BERT

Vectoriza texto para búsqueda semántica.

## Por qué en minerOS

Convierte párrafos en vectores matemáticos. Permite buscar 'documentos similares a este' sin keywords exactas.

## Casos de uso

- Knowledge Base RAG
- Búsqueda en notas
- Clustering de documentos

## Código ejemplo

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
vector = model.encode('Tu texto aquí')
```

## Proyectos que lo usan

- DirectOS v6.0 (Knowledge Base)
- DocMine-Fiscal (búsqueda semántica facturas)
