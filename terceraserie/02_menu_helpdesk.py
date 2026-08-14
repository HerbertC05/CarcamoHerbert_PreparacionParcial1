"""
Ejercicio 2: Menu modular de tickets en memoria
Semana 1 - Refactoriza el registro anterior en un programa modular
que mantenga varios tickets durante la ejecucion.
"""

CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]

tickets = []  # Lista de diccionarios en memoria
contador_id = 1  # Autoincremental simple para numero de ticket


def pedir_opcion():
    """Muestra el menu principal y devuelve la opcion elegida por el usuario."""
    print("\n=== Menu HelpDesk EDU ===")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Mostrar resumen por prioridad")
    print("5. Salir")
    opcion = input("Seleccione una opcion (1-5): ").strip()
    return opcion


def pedir_texto_obligatorio(mensaje):
    """Solicita un campo de texto y rechaza valores vacios."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: este campo es obligatorio y no puede quedar vacio.")
        else:
            return valor


def pedir_categoria():
    """Solicita la categoria y valida contra la lista de categorias validas."""
    while True:
        categoria = input(f"Categoria {CATEGORIAS_VALIDAS}: ").strip().capitalize()
        if categoria in CATEGORIAS_VALIDAS:
            return categoria
        print(f"Error: categoria invalida. Opciones validas: {CATEGORIAS_VALIDAS}")


def pedir_prioridad():
    """Solicita la prioridad y valida contra la lista de prioridades validas."""
    while True:
        prioridad = input(f"Prioridad {PRIORIDADES_VALIDAS}: ").strip().capitalize()
        if prioridad in PRIORIDADES_VALIDAS:
            return prioridad
        print(f"Error: prioridad invalida. Opciones validas: {PRIORIDADES_VALIDAS}")


def registrar_ticket():
    """Solicita los datos de un ticket y lo agrega a la lista global con append()."""
    global contador_id

    solicitante = pedir_texto_obligatorio("Solicitante: ")
    titulo = pedir_texto_obligatorio("Titulo: ")
    descripcion = pedir_texto_obligatorio("Descripcion: ")
    categoria = pedir_categoria()
    prioridad = pedir_prioridad()

    ticket = {
        "numero": contador_id,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open",
    }

    tickets.append(ticket)
    contador_id += 1
    print(f"Ticket #{ticket['numero']} registrado con exito.\n")


def listar_tickets():
    """Muestra todos los tickets registrados hasta el momento."""
    if len(tickets) == 0:
        print("No hay tickets registrados todavia.\n")
        return

    print("\n--- Lista de tickets ---")
    for t in tickets:
        print(
            f"#{t['numero']} | {t['titulo']} | {t['categoria']} | "
            f"{t['prioridad']} | {t['status']} | Solicitante: {t['solicitante']}"
        )
    print("------------------------\n")

# Busca tickets por solicitante sin distinguir mayusculas/minusculas
def buscar_por_solicitante():
    """Busca tickets cuyo solicitante coincida (sin distinguir mayusculas/minusculas)."""
    nombre = input("Nombre del solicitante a buscar: ").strip().lower()

    encontrados = []
    for t in tickets:
        if t["solicitante"].lower() == nombre:
            encontrados.append(t)

    if len(encontrados) == 0:
        print(f"No se encontraron tickets para el solicitante '{nombre}'.\n")
        return

    print(f"\n--- Tickets de '{nombre}' ---")
    for t in encontrados:
        print(f"#{t['numero']} | {t['titulo']} | {t['prioridad']} | {t['status']}")
    print("-----------------------------\n")


def mostrar_resumen_por_prioridad():
    """Cuenta y muestra cuantos tickets hay por cada nivel de prioridad."""
    conteo = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}

    for t in tickets:
        conteo[t["prioridad"]] += 1

    print("\n--- Resumen por prioridad ---")
    for prioridad, cantidad in conteo.items():
        print(f"{prioridad}: {cantidad} ticket(s)")
    print(f"Total: {len(tickets)} ticket(s)")
    print("------------------------------\n")


def ejecutar_menu():
    """Bucle principal que ejecuta el menu hasta que el usuario decida salir."""
    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket()
        elif opcion == "2":
            listar_tickets()
        elif opcion == "3":
            buscar_por_solicitante()
        elif opcion == "4":
            mostrar_resumen_por_prioridad()
        elif opcion == "5":
            print("Saliendo del programa. Hasta luego.")
            break
        else:
            print("Opcion invalida. Por favor seleccione un numero del 1 al 5.\n")


if __name__ == "__main__":
    ejecutar_menu()