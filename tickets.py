from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from google import genai
from typing import Literal
from typing import List

load_dotenv()
mi_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=mi_key)
app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola, funciona"}

class Ticket(BaseModel):
    categoria: Literal["acceso", "facturacion", "bug", "otros"]
    sentimiento: Literal["positivo", "negativo", "neutral"]
    urgencia: Literal["baja", "media", "alta"]
    resumen : str
class TicketEntrada(BaseModel):
    texto: str

@app.post("/tickets")
def analizar_ticket(ticket: TicketEntrada):
    resultado = client.models.generate_content(
         model="gemini-3.6-flash",
    contents=f"Analiza este ticket: {ticket.texto}",
    config={
        "response_mime_type": "application/json",
        "response_schema": Ticket,
    }
    )
    texto_json = resultado.parsed.model_dump_json()
    with open("tickets_historial.jsonl", "a", encoding="utf-8") as f:
        f.write(texto_json + "\n")
    return resultado.parsed
