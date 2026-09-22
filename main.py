from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel
from typing import Literal
from typing import List
load_dotenv()
mi_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=mi_key)

class DatoCurioso(BaseModel):
    dato: str
    fuente_confiable: bool 
class ListaDatos(BaseModel):
    datos: List[str]
    nivel_certeza: Literal["alto", "medio", "bajo"]
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="dime 3 datos curiosos sobre el espacio, y su nivel de certeza",
    config={
        "response_mime_type": "application/json",
        "response_schema": ListaDatos,
    }
)

print(response.parsed)