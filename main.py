from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel

load_dotenv()
mi_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=mi_key)

class DatoCurioso(BaseModel):
    dato: str
    fuente_confiable: bool 
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Dime un dato curioso del espacio",
    config={
        "response_mime_type": "application/json",
        "response_schema": DatoCurioso,
    }
)

print(response.text)