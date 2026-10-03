from tickets import Ticket
ticket_prueba = Ticket(
    categoria="bug",
    sentimiento="negativo",
    urgencia="alta",
    resumen="La app se cierra al abrir el perfil"
)
texto_json = ticket_prueba.model_dump_json()
with open("tickets_historial.jsonl", "a") as f:
    f.write(texto_json + "\n")