---
id: output-file
name: Output File
category: Output
icon: fa-file-export
color: text-orange-400
tag: Guardar Archivo
status: new
level: solid
next: Output Notify para notificaciones
isOutput: true
---

# Output File

Guarda el resultado del pipeline en un archivo.

## Por qué en minerOS

El paso final de muchos pipelines: guardar el resultado procesado en disco. PDFs, JSONs, CSVs, o cualquier formato.

## Casos de uso

- Guardar resumen en markdown
- Exportar datos a CSV
- Generar reporte PDF
- Backup de resultados

## Código ejemplo

```python
from pathlib import Path
import json

def save_output(data, filename, format='json'):
    """Guarda resultado del pipeline en archivo"""
    output_path = Path(f"./output/{filename}")
    output_path.parent.mkdir(exist_ok=True)

    if format == 'json':
        output_path.write_text(json.dumps(data, indent=2))
    elif format == 'txt':
        output_path.write_text(str(data))
    elif format == 'csv':
        import csv
        with open(output_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    return str(output_path)
```

## Tips aprendidos

- Crear directorio output/ si no existe
- Añadir timestamp al nombre para evitar sobreescribir
- Validar formato antes de guardar

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
