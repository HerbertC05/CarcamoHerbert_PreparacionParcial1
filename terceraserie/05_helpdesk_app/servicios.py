"""
servicios.py - Logica de negocio del sistema HelpDesk EDU
Ejercicio 5 - Contiene registrar_ticket(), listar_tickets(), buscar_ticket(),
asignar_tecnico() y cambiar_estado(). No incluye el menu.
"""

from modelos import Ticket

tickets = []  # Lista de objetos Ticket en memoria
contador_id = 1  # Autoincremental simple


def registrar_ticket(titulo, categoria, prioridad, solicitante):
    """Crea un nuevo Ticket, lo agrega a la lista y evita duplicar logica."""
    global contador_id

    nuevo_ticket = Ticket(contador_id, titulo, categoria, prioridad, solicitante)
    tickets.append(nuevo_ticket)
    contador_id += 1
    return nuevo_ticket


def listar_tickets():
    """Devuelve la lista completa de tickets registrados."""
    return tickets


def buscar_ticket(id_ticket):
    """Busca un ticket por su id. Devuelve el objeto Ticket o None si no existe."""
    for t in tickets:
        if t.id == id_ticket:
            return t
    return None


def asignar_tecnico(id_ticket, tecnico):
    """Asigna un tecnico a un ticket existente, buscandolo primero por id."""
    ticket = buscar_ticket(id_ticket)
    if ticket is None:
        return False
    return ticket.asignar_tecnico(tecnico)


def cambiar_estado(id_ticket, nuevo_estado):
    """Cambia el estado de un ticket existente, buscandolo primero por id."""
    ticket = buscar_ticket(id_ticket)
    if ticket is None:
        return False
    return ticket.cambiar_estado(nuevo_estado)