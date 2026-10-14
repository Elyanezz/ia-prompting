import json

tickets = []
with open("tickets_historial.jsonl", "r", encoding="utf-8") as f:
    for linea in f:
        ticket = json.loads(linea)
        tickets.append(ticket)

urgentes = [ticket for ticket in tickets if ticket["urgencia"] == "alta"]
print("Urgentes:", len(urgentes))
conteo = {}
for ticket in tickets:
    categoria = ticket["categoria"]
    if categoria not in conteo:
        conteo[categoria] = 0
    conteo[categoria] += 1

for categoria, valor in conteo.items():
    print(f"{categoria}: {valor}")