"""
Ejercicio 3: Modelo orientado a objetos
Semana 2 - Representa usuarios y tickets mediante clases con estado,
comportamiento y colecciones de objetos.
"""

ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]


class Usuario:
    """Representa a un usuario del sistema HelpDesk EDU."""

    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol  # ej: "solicitante" o "technician"

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
        self._status = "Open"  # estado encapsulado
# Cambia el estado del ticket solo si es un estado valido de la lista
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del ticket si es un estado valido."""
        if nuevo_estado not in ESTADOS_VALIDOS:
            print(f"Error: '{nuevo_estado}' no es un estado valido. "
                  f"Estados validos: {ESTADOS_VALIDOS}")
            return False
        self._status = nuevo_estado
        return True
# Asigna un tecnico al ticket solo si su rol es 'technician'
    def asignar_tecnico(self, tecnico):
        """Asigna un tecnico al ticket, validando que su rol sea 'technician'."""
        if tecnico.rol != "technician":
            print(f"Error: {tecnico.nombre} no tiene el rol 'technician', "
                  f"no puede ser asignado como tecnico.")
            return False
        self.tecnico = tecnico
        return True

    def __str__(self):
        tecnico_str = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (f"Ticket #{self.id} | {self.titulo} | {self.categoria} | "
                f"{self.prioridad} | Estado: {self._status} | "
                f"Solicitante: {self.solicitante.nombre} | Tecnico: {tecnico_str}")

# Crea usuarios y tickets de prueba, y demuestra el flujo completo
def main():
    # Crear dos usuarios
    usuario1 = Usuario(1, "Ana Lopez", "ana@correo.com", "solicitante")
    usuario2 = Usuario(2, "Carlos Ruiz", "carlos@correo.com", "technician")

    # Crear tres tickets
    ticket1 = Ticket(101, "Wifi caido", "Network", "Critical", usuario1)
    ticket2 = Ticket(102, "Error de login", "Software", "Medium", usuario1)
    ticket3 = Ticket(103, "Mouse dañado", "Hardware", "Low", usuario1)

    tickets = [ticket1, ticket2, ticket3]

    print("=== Tickets creados ===")
    for t in tickets:
        print(t)

    print("\n=== Asignando tecnico al ticket 101 ===")
    ticket1.asignar_tecnico(usuario2)

    print("\n=== Cambiando ticket 101 a 'In Progress' ===")
    ticket1.cambiar_estado("In Progress")

    print("\n=== Intentando un estado no permitido ===")
    ticket1.cambiar_estado("Pausado")  # Estado invalido, debe rechazarse

    print("\n=== Estado final de los tickets ===")
    for t in tickets:
        print(t)


if __name__ == "__main__":
    main()