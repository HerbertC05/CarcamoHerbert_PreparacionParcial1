# Serie III — Práctica en Visual Studio Code

Cinco ejercicios de 10 puntos cada uno. Python estándar y almacenamiento en memoria.

---

## Ejercicio 1 — Registro de un ticket por consola (Semana 1)

**Objetivo:** Construir un primer registro usando entrada, conversión,
condicionales, listas y diccionarios.

**Archivo(s):** `01_registro_ticket.py`

**Requisitos cumplidos:**
- Solicita número de ticket, solicitante, título, descripción, categoría y prioridad.
- Valida el número con `try/except ValueError` y rechaza campos obligatorios vacíos.
- Valida categorías (`General`, `Hardware`, `Software`, `Network`) y prioridades
  (`Low`, `Medium`, `High`, `Critical`).
- Guarda el registro en un diccionario con estado inicial `Open`.
- Muestra un resumen con f-strings.

**Evidencia de ejecución:** ver capturas de pantalla en el documento de Word entregado.

---

## Ejercicio 2 — Menú modular de tickets en memoria (Semana 1)

**Objetivo:** Refactorizar el registro anterior como un programa modular
que mantenga varios tickets durante la ejecución.

**Archivo(s):** `02_menu_helpdesk.py`

**Requisitos cumplidos:**
- Implementa `pedir_opcion()`, `registrar_ticket()`, `listar_tickets()`,
  `buscar_por_solicitante()`, `mostrar_resumen()` (resumen por prioridad) y
  `ejecutar_menu()`.
- Usa una lista de diccionarios y agrega registros con `append()`.
- Menú: registrar, listar, buscar por solicitante, resumen por prioridad y salir.
- Usa `while`, `if/elif/else`, `for`, `len()` y comparación sin distinguir
  mayúsculas/minúsculas.
- Incluye `if __name__ == "__main__":` para iniciar el menú.

**Evidencia de ejecución:** ver capturas de pantalla en el documento de Word entregado.

---

## Ejercicio 3 — Modelo orientado a objetos (Semana 2)

**Objetivo:** Representar usuarios y tickets mediante clases con estado,
comportamiento y colecciones de objetos.

**Archivo(s):** `03_modelos.py`

**Requisitos cumplidos:**
- Clase `Usuario` con id, nombre, email y rol; clase `Ticket` con id, título,
  categoría, prioridad, solicitante, técnico opcional y estado.
- Utiliza `__init__`, `self` y `__str__` en ambas clases.
- Encapsula el estado como `_status` y lo cambia mediante `cambiar_estado()`.
- Estados válidos: `Open`, `In Progress`, `Resolved`, `Closed`, `Cancelled`.
- Implementa `asignar_tecnico(tecnico)` y valida que el rol sea `technician`.
- Crea dos usuarios y tres tickets, almacenados en una lista de objetos, e imprime.

**Evidencia de ejecución:** ver capturas de pantalla en el documento de Word entregado.

---

## Ejercicio 4 — UML y relaciones del dominio HelpDesk EDU (Semanas 3 y 4)

**Objetivo:** Diseñar un modelo coherente y relacionarlo con esqueletos
Python, sin persistencia ni frameworks.

**Archivo(s):** `04_modelo_helpdesk.puml`, `04_modelos_base.py`,
`04_justificacion_relaciones.md`

**Requisitos cumplidos:**
- Modela `User`, `Ticket`, `Comment`, `History` y `Article` con atributos y
  al menos un método relevante.
- Representa `User "1" -- "0..*" Ticket` (solicitante) y
  `User "0..1" -- "0..*" Ticket` (técnico opcional).
- Representa `Ticket "1" *-- "0..*" Comment` y `Ticket "1" *-- "0..*" History`
  como composiciones.
- Representa `User "1" -- "0..*" Article` como asociación.
- Crea esqueletos Python consistentes con el diagrama.
- Justifica cada relación, multiplicidad y criterio de ciclo de vida.

**Evidencia de ejecución:** ver capturas de pantalla del diagrama renderizado
(rombos negros del lado de `Ticket`) en el documento de Word entregado.

---

## Ejercicio 5 — Miniaplicación HelpDesk organizada por módulos (Semana 5)

**Objetivo:** Integrar consola, modularidad, POO, relaciones y estructura
de programa en una solución pequeña y ejecutable.

**Archivo(s):** Carpeta `05_helpdesk_app/` con `modelos.py`, `servicios.py`,
`main.py` y `README.md`

**Requisitos cumplidos:**
- `modelos.py` contiene las clases `Usuario` y `Ticket`; no incluye el menú.
- `servicios.py` contiene `registrar_ticket()`, `listar_tickets()`,
  `buscar_ticket()`, `asignar_tecnico()` y `cambiar_estado()`.
- `main.py` implementa el menú, importa modelos y servicios, y usa
  `if __name__ == "__main__":`.
- Trabaja con una lista de objetos `Ticket` y evita duplicar lógica.
- Flujo probado: crear solicitante y técnico, registrar ticket, asignarlo,
  cambiar su estado y listarlo.

**Evidencia de ejecución:** ver capturas de pantalla del flujo completo en el
documento de Word entregado.

---

## Repositorio

Repositorio de GitHub: https://github.com/HerbertC05/CarcamoHerbert_PreparacionParcial1