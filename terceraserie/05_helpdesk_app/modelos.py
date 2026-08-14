"""
modelos.py - Clases del dominio HelpDesk EDU
Ejercicio 5 - Solo contiene las clases Usuario y Ticket, sin logica de menu.
"""

ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]


class Usuario:
    """Representa a un usuario del sistema: solicitante o tecnico."""

    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol  # "solicitante" o "technician"

    def __str__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, rol={self.rol})"


class Ticket:
    """Representa un ticket de soporte con estado encapsulado."""

    def __init__(self, id_ticket, titulo, categoria, prioridad, solicitante):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante  # objeto Usuario
        self.tecnico = None  # objeto Usuario opcional
        self._status = "Open"

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del ticket si es valido. Devuelve True/False."""
        if nuevo_estado not in ESTADOS_VALIDOS:
            return False
        self._status = nuevo_estado
        return True

    def asignar_tecnico(self, tecnico):
        """Asigna un tecnico al ticket si su rol es 'technician'."""
        if tecnico.rol != "technician":
            return False
        self.tecnico = tecnico
        return True

    def obtener_estado(self):
        """Devuelve el estado actual del ticket (encapsulado)."""
        return self._status

    def __str__(self):
        tecnico_str = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (f"Ticket #{self.id} | {self.titulo} | {self.categoria} | "
                f"{self.prioridad} | Estado: {self._status} | "
                f"Solicitante: {self.solicitante.nombre} | Tecnico: {tecnico_str}")