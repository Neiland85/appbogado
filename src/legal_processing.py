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

def leer_texto_legal(ruta_archivo):
    # Implementación de la función
    with open(ruta_archivo, 'r') as file:
        return file.read()

def procesar_texto_legal(texto):
    # Implementación de la función
    pass

def limpiar_texto(texto):
    # Implementación de la función
    pass
