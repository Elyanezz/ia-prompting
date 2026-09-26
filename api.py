from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola, funciona"}

class Reseña(BaseModel):
    texto: str

@app.post("/analizar")
def analizar(reseña: Reseña):
    return {"recibido": reseña.texto}