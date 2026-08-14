"""
Ejercicio 1: Registro de un ticket por consola
Semana 1 - Construye un primer registro usando entrada, conversion,
condicionales, listas y diccionarios.
"""

CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]


def pedir_numero_ticket():
    """Solicita el numero de ticket y valida que sea un entero."""
    while True:
        entrada = input("Numero de ticket: ").strip()
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Error: el numero de ticket debe ser un valor entero. Intente de nuevo.")


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
    """Solicita todos los datos del ticket y construye el diccionario del registro."""
    numero = pedir_numero_ticket()
    solicitante = pedir_texto_obligatorio("Solicitante: ")
    titulo = pedir_texto_obligatorio("Titulo: ")
    descripcion = pedir_texto_obligatorio("Descripcion: ")
    categoria = pedir_categoria()
    prioridad = pedir_prioridad()

    ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open",
    }
    return ticket


def mostrar_resumen(ticket):
    """Muestra un resumen del ticket registrado usando f-strings."""
    print("\n--- Resumen del ticket registrado ---")
    print(f"Ticket #{ticket['numero']} | Estado: {ticket['status']}")
    print(f"Solicitante: {ticket['solicitante']}")
    print(f"Titulo: {ticket['titulo']}")
    print(f"Descripcion: {ticket['descripcion']}")
    print(f"Categoria: {ticket['categoria']} | Prioridad: {ticket['prioridad']}")
    print("--------------------------------------\n")


def main():
    print("=== Registro de un nuevo ticket ===\n")
    ticket = registrar_ticket()
    mostrar_resumen(ticket)


if __name__ == "__main__":
    main()