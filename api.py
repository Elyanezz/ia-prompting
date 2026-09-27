from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel
from typing import Literal
from typing import List

load_dotenv()
mi_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=mi_key)
app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola, funciona"}

class Reseña(BaseModel):
    texto: str
class Reseñas(BaseModel):
    sentimiento: Literal["positivo", "negativo", "neutral"]
    resumen : str
    requiere_atencion: bool 


@app.post("/analizar")
def analizar(reseña: Reseña):
    resultado = client.models.generate_content(
         model="gemini-3.6-flash",
    contents=f"Analiza esta reseña: {reseña.texto}",
    config={
        "response_mime_type": "application/json",
        "response_schema": Reseñas,
    }
    )
    return resultado.parsed