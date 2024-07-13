# src/legal_processing.py
import openai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def detectar_mentiras(texto):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Detecta mentiras en el siguiente texto: {texto}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def detectar_difamaciones(texto):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Detecta difamaciones en el siguiente texto: {texto}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

