# Justificación de relaciones — Modelo HelpDesk EDU

## 1. User "1" -- "0..*" Ticket (solicita)

**Tipo de relación:** Asociación simple.

**Multiplicidad:** Un `User` (solicitante) puede registrar cero o muchos `Ticket`,
pero cada `Ticket` debe tener exactamente un solicitante (obligatorio).

**Justificación:** Un usuario puede no haber creado ningún ticket todavía,
o puede haber creado varios a lo largo del tiempo. Sin embargo, todo ticket
necesita un solicitante que lo haya generado; no puede existir un ticket
huérfano sin usuario asociado.

**Ciclo de vida:** Independiente. Si se elimina un `User`, sus `Ticket` no
desaparecen automáticamente (podrían reasignarse o archivarse), por lo que
no es una composición.

---

## 2. User "0..1" -- "0..*" Ticket (atiende)

**Tipo de relación:** Asociación simple.

**Multiplicidad:** Un `Ticket` puede tener cero o un técnico asignado
(0..1), y un `User` con rol técnico puede atender cero o muchos tickets (0..*).

**Justificación:** Un ticket recién creado puede no tener técnico asignado
todavía (queda en cola), y un técnico puede estar manejando varios tickets
a la vez.

**Ciclo de vida:** Independiente. El técnico existe con o sin tickets
asignados.

---

## 3. Ticket "1" *-- "0..*" Comment (contiene)

**Tipo de relación:** Composición (rombo negro del lado de `Ticket`).

**Multiplicidad:** Un `Ticket` puede tener cero o muchos `Comment`, pero
cada `Comment` pertenece exactamente a un `Ticket`.

**Justificación:** Los comentarios solo tienen sentido en el contexto del
ticket al que pertenecen; no existen de forma independiente.

**Ciclo de vida:** Dependiente. Si el `Ticket` se elimina, sus `Comment`
se eliminan junto con él — de ahí que sea composición y no asociación.

---

## 4. Ticket "1" *-- "0..*" History (registra)

**Tipo de relación:** Composición (rombo negro del lado de `Ticket`).

**Multiplicidad:** Un `Ticket` puede tener cero o muchos registros de
`History`, pero cada `History` pertenece a un único `Ticket`.

**Justificación:** El historial documenta los cambios de un ticket
específico (cambios de estado, asignaciones, etc.); no tiene utilidad
fuera de ese ticket.

**Ciclo de vida:** Dependiente. El historial de un ticket desaparece si
el ticket se elimina, reforzando la composición.

---

## 5. User "1" -- "0..*" Article (publica)

**Tipo de relación:** Asociación simple.

**Multiplicidad:** Un `User` (autor) puede publicar cero o muchos
`Article`, pero cada `Article` tiene exactamente un autor.

**Justificación:** Los artículos de la base de conocimiento son escritos
por un usuario, pero a diferencia de los comentarios, un artículo puede
seguir existiendo y siendo consultado incluso si el autor original
cambia de rol o dejara el sistema — por eso es asociación y no
composición.

**Ciclo de vida:** Independiente. El `Article` no depende del `User`
para seguir existiendo en la base de conocimiento.