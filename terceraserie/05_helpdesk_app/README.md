# HelpDesk EDU — Mini aplicación modular

## Ejercicio 5 — Semana 5 e integración

Mini aplicación de consola que integra POO, relaciones entre clases y
estructura modular de programa, sin persistencia ni frameworks externos.

## Estructura del proyecto
05_helpdesk_app/
├── modelos.py # Clases Usuario y Ticket (sin lógica de menú)
├── servicios.py # Lógica de negocio: registrar, buscar, asignar, cambiar estado
├── main.py # Punto de entrada: menú interactivo
└── README.md # Este archivo


## Cómo ejecutar

Desde dentro de esta carpeta (`05_helpdesk_app`), ejecutar:
python main.py


## Flujo mínimo probado

1. Crear un solicitante (opción 1)
2. Crear un técnico (opción 2)
3. Registrar un ticket asociado al solicitante (opción 3)
4. Asignar el técnico al ticket (opción 4)
5. Cambiar el estado del ticket (opción 5)
6. Listar los tickets para verificar los cambios (opción 6)
7. Salir del programa (opción 7)

## Separación de responsabilidades

- `modelos.py`: define únicamente las clases y su comportamiento propio
  (encapsulamiento del estado, validaciones internas).
- `servicios.py`: contiene la lógica de negocio que opera sobre listas de
  objetos en memoria (registrar, buscar, asignar, cambiar estado).
- `main.py`: se encarga solo de la interacción con el usuario (menú) y
  conecta `modelos.py` con `servicios.py`, evitando duplicar lógica.



