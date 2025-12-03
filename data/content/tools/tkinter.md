---
id: tkinter
name: Tkinter
category: Frontend
icon: fa-window-maximize
color: text-blue-300
tag: GUI Desktop
status: used
level: working
next: CustomTkinter moderno
---

# Tkinter

Librería GUI estándar de Python. Interfaces de escritorio sin dependencias.

## Por qué en minerOS

Viene incluida con Python. Perfecta para herramientas de escritorio simples y rápidas.

## Casos de uso

- Aplicaciones de escritorio
- Herramientas de productividad
- Interfaces para scripts
- Selectores de archivos

## Código ejemplo

```python
import tkinter as tk
from tkinter import filedialog, ttk

def select_files():
    files = filedialog.askopenfilenames(
        title="Seleccionar PDFs",
        filetypes=[("PDF files", "*.pdf")]
    )
    for f in files:
        listbox.insert(tk.END, f)

root = tk.Tk()
root.title("Limpiador PDFs")

btn = ttk.Button(root, text="Seleccionar archivos", command=select_files)
btn.pack(pady=10)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

root.mainloop()
```

## Proyectos que lo usan

- Limpiador PDFs (interfaz de selección)
