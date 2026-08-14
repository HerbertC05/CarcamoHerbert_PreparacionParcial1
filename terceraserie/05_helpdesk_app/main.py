"""
main.py - Punto de entrada del sistema HelpDesk EDU
Ejercicio 5 - Implementa el menu, importa modelos y servicios,
y usa if __name__ == "__main__".
"""

from modelos import Usuario
import servicios

usuarios = []  # Lista de objetos Usuario en memoria
contador_usuario_id = 1


def crear_usuario(nombre, email, rol):
    """Crea un nuevo Usuario y lo agrega a la lista en memoria."""
    global contador_usuario_id
    usuario = Usuario(contador_usuario_id, nombre, email, rol)
    usuarios.append(usuario)
    contador_usuario_id += 1
    return usuario


def buscar_usuario_por_nombre(nombre):
    """Busca un usuario por nombre (sin distinguir mayusculas/minusculas)."""
    for u in usuarios:
        if u.nombre.lower() == nombre.lower():
            return u
    return None


def mostrar_menu():
    """Muestra las opciones del menu principal."""
    print("\n=== HelpDesk EDU - Mini aplicacion modular ===")
    print("1. Crear solicitante")
    print("2. Crear tecnico")
    print("3. Registrar ticket")
    print("4. Asignar tecnico a un ticket")
    print("5. Cambiar estado de un ticket")
    print("6. Listar tickets")
    print("7. Salir")


def flujo_crear_usuario(rol):
    """Solicita datos y crea un usuario con el rol indicado."""
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    usuario = crear_usuario(nombre, email, rol)
    print(f"Usuario creado: {usuario}")


def flujo_registrar_ticket():
    """Solicita datos y registra un ticket asociado a un solicitante existente."""
    if len(usuarios) == 0:
        print("Primero debes crear al menos un usuario (solicitante).\n")
        return

    nombre_solicitante = input("Nombre del solicitante: ").strip()
    solicitante = buscar_usuario_por_nombre(nombre_solicitante)
    if solicitante is None:
        print("Ese solicitante no existe. Crealo primero con la opcion 1.\n")
        return

    titulo = input("Titulo del ticket: ").strip()
    categoria = input("Categoria: ").strip()
    prioridad = input("Prioridad: ").strip()

    ticket = servicios.registrar_ticket(titulo, categoria, prioridad, solicitante)
    print(f"Ticket creado: {ticket}")


def flujo_asignar_tecnico():
    """Solicita id de ticket y nombre de tecnico para asignarlo."""
    id_ticket = int(input("ID del ticket: ").strip())
    nombre_tecnico = input("Nombre del tecnico: ").strip()

    tecnico = buscar_usuario_por_nombre(nombre_tecnico)
    if tecnico is None:
        print("Ese tecnico no existe. Crealo primero con la opcion 2.\n")
        return

    exito = servicios.asignar_tecnico(id_ticket, tecnico)
    if exito:
        print(f"Tecnico {tecnico.nombre} asignado al ticket #{id_ticket}.")
    else:
        print("No se pudo asignar el tecnico (verifica el rol o el id del ticket).")


def flujo_cambiar_estado():
    """Solicita id de ticket y nuevo estado para actualizarlo."""
    id_ticket = int(input("ID del ticket: ").strip())
    nuevo_estado = input("Nuevo estado: ").strip()

    exito = servicios.cambiar_estado(id_ticket, nuevo_estado)
    if exito:
        print(f"Estado del ticket #{id_ticket} actualizado a '{nuevo_estado}'.")
    else:
        print("No se pudo cambiar el estado (verifica el estado o el id del ticket).")


def flujo_listar_tickets():
    """Muestra todos los tickets registrados."""
    tickets = servicios.listar_tickets()
    if len(tickets) == 0:
        print("No hay tickets registrados todavia.\n")
        return

    print("\n--- Lista de tickets ---")
    for t in tickets:
        print(t)
    print("------------------------\n")


def ejecutar_menu():
    """Bucle principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-7): ").strip()

        if opcion == "1":
            flujo_crear_usuario("solicitante")
        elif opcion == "2":
            flujo_crear_usuario("technician")
        elif opcion == "3":
            flujo_registrar_ticket()
        elif opcion == "4":
            flujo_asignar_tecnico()
        elif opcion == "5":
            flujo_cambiar_estado()
        elif opcion == "6":
            flujo_listar_tickets()
        elif opcion == "7":
            print("Saliendo del programa. Hasta luego.")
            break
        else:
            print("Opcion invalida. Intente de nuevo.\n")


if __name__ == "__main__":
    ejecutar_menu()