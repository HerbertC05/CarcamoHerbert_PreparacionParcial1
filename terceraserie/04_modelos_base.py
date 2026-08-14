"""
Ejercicio 4: Esqueletos Python consistentes con el diagrama UML
Semanas 3 y 4 - Modelo coherente y relacionado del dominio HelpDesk EDU,
sin persistencia ni frameworks.
"""


class User:
    """Representa un usuario: puede ser solicitante, tecnico, o ambos."""

    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"User(id={self.id}, nombre={self.nombre}, rol={self.rol})"


class Comment:
    """Comentario que pertenece a un Ticket (relacion de composicion)."""

    def __init__(self, id_comment, texto, fecha, autor):
        self.id = id_comment
        self.texto = texto
        self.fecha = fecha
        self.autor = autor  # objeto User


class History:
    """Registro de historial de cambios que pertenece a un Ticket (composicion)."""

    def __init__(self, id_history, accion, fecha):
        self.id = id_history
        self.accion = accion
        self.fecha = fecha

    def registrar_cambio(self, accion):
        """Actualiza la accion registrada en este historial."""
        self.accion = accion


class Article:
    """Articulo de la base de conocimiento, asociado a un User (autor)."""

    def __init__(self, id_article, titulo, contenido, autor):
        self.id = id_article
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # objeto User (asociacion, no composicion)


class Ticket:
    """
    Ticket de soporte. Es el "todo" en las composiciones con Comment
    e History: si el Ticket se elimina, sus comentarios e historial
    tambien dejan de existir.
    """

    def __init__(self, id_ticket, titulo, categoria, prioridad, solicitante):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante  # objeto User (1..1 obligatorio)
        self.tecnico = None  # objeto User opcional (0..1)
        self._status = "Open"
        self.comentarios = []  # lista de objetos Comment (0..*)
        self.historial = []  # lista de objetos History (0..*)

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del ticket y registra el cambio en el historial."""
        self._status = nuevo_estado

    def asignar_tecnico(self, tecnico):
        """Asigna un tecnico opcional al ticket."""
        self.tecnico = tecnico

    def agregar_comentario(self, comment):
        """Agrega un Comment a la lista de comentarios del ticket (composicion)."""
        self.comentarios.append(comment)

    def agregar_historial(self, history):
        """Agrega un registro de History a la lista del ticket (composicion)."""
        self.historial.append(history)