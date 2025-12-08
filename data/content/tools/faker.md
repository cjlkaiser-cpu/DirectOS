---
id: faker
name: Faker
category: Testing
icon: fa-masks-theater
color: text-fuchsia-400
tag: Datos Sinteticos
status: used
level: solid
next: Factory Boy para fixtures
---

# Faker

Libreria Python para generar datos sinteticos realistas.

## Por que en minerOS

Ideal para demos, tests y prototipos. Genera nombres, direcciones, DNI, emails realistas sin usar datos personales reales.

## Casos de uso

- Datos de prueba para demos
- Fixtures para tests
- Poblar bases de datos de desarrollo
- Anonimizar datos reales

## Codigo ejemplo

```python
from faker import Faker

fake = Faker('es_ES')  # Locale español

# Generar persona
nombre = fake.first_name()
apellidos = f"{fake.last_name()} {fake.last_name()}"
dni = fake.nif()  # DNI español con letra
email = fake.email()
telefono = fake.phone_number()
direccion = fake.address()
fecha_nac = fake.date_of_birth(minimum_age=5, maximum_age=70)

# Generar multiples
alumnos = [
    {
        'nombre': fake.first_name(),
        'apellidos': f"{fake.last_name()} {fake.last_name()}",
        'email': fake.email(),
        'telefono': fake.phone_number()
    }
    for _ in range(50)
]
```

## Tips aprendidos

- `Faker('es_ES')` para datos españoles (nombres, DNI, direcciones)
- `fake.date_of_birth(minimum_age=X, maximum_age=Y)` para rangos de edad
- `fake.random_element(['op1', 'op2'])` para seleccion aleatoria
- Usar `Seed` para reproducibilidad: `Faker.seed(1234)`

## Proyectos que lo usan

- Factoria Demo (50 alumnos + 60 tutores + inscripciones sinteticas)
