from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel
from typing import Literal
from typing import List
load_dotenv()
mi_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=mi_key)

class Reseñas(BaseModel):
    sentimiento: Literal["positivo", "negativo", "neutral"]
    resumen : str
    requiere_atencion: bool 
reseñas = [
    "El producto llegó roto y nadie me responde los emails",
    "Todo perfecto, llegó rápido y como se describía",
    "Está bien, nada especial"
]
for reseña in reseñas:
    resultado = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Analiza esta reseña: {reseña}",
    config={
        "response_mime_type": "application/json",
        "response_schema": Reseñas,
    }
    )
    print(resultado.parsed)