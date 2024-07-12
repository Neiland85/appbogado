import re
from collections import Counter
from spacy import load
from textblob import TextBlob

nlp = load('es_core_news_md')

def leer_texto_legal(ruta_archivo):
    """
    Lee el contenido de un archivo de texto legal.
    
    Args:
        ruta_archivo (str): Ruta al archivo de texto legal.
    
    Returns:
        str: Contenido del archivo.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return file.read()

def limpiar_texto(texto):
    """
    Limpia el texto eliminando caracteres no deseados y normalizando el contenido.
    
    Args:
        texto (str): Texto a limpiar.
    
    Returns:
        str: Texto limpio.
    """
    texto_limpio = re.sub(r'\s+', ' ', texto)  # Elimina espacios en blanco adicionales
    texto_limpio = re.sub(r'[^\w\s]', '', texto_limpio)  # Elimina caracteres no alfanuméricos
    return texto_limpio.strip()

def procesar_texto_legal(texto):
    """
    Procesa el texto legal utilizando un modelo NLP.
    
    Args:
        texto (str): Texto legal a procesar.
    
    Returns:
        Doc: Documento procesado por spaCy.
    """
    return nlp(texto)

def identificar_entidades(doc):
    """
    Identifica entidades en un documento procesado.
    
    Args:
        doc (Doc): Documento procesado por spaCy.
    
    Returns:
        list: Lista de entidades identificadas.
    """
    return [(ent.text, ent.label_) for ent in doc.ents]

def detectar_sentencias_clave(doc):
    """
    Detecta sentencias clave en un documento procesado.
    
    Args:
        doc (Doc): Documento procesado por spaCy.
    
    Returns:
        list: Lista de sentencias clave.
    """
    return [sent.text for sent in doc.sents if 'clave' in sent.text]

def analizar_sentimiento(texto):
    """
    Analiza el sentimiento del texto.
    
    Args:
        texto (str): Texto a analizar.
    
    Returns:
        str: Sentimiento predominante ('positivo', 'neutral', 'negativo').
    """
    analysis = TextBlob(texto)
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negativo'

def detectar_anomalias(texto):
    """
    Detecta anomalías en el texto utilizando heurísticas simples.
    
    Args:
        texto (str): Texto a analizar.
    
    Returns:
        list: Lista de anomalías detectadas.
    """
    palabras = texto.split()
    palabra_mas_comun, frecuencia = Counter(palabras).most_common(1)[0]
    if frecuencia > len(palabras) * 0.2:  # Si una palabra aparece en más del 20% del texto, es una anomalía
        return [palabra_mas_comun]
    return []

def detectar_difamacion(texto):
    """
    Detecta posibles difamaciones en el texto.
    
    Args:
        texto (str): Texto a analizar.
    
    Returns:
        bool: True si se detecta difamación, False de lo contrario.
    """
    palabras_clave_difamacion = ['calumnia', 'difamación', 'injuria']
    return any(palabra in texto for palabra in palabras_clave_difamacion)

def detectar_ayuda_y_compañerismo(texto):
    """
    Detecta términos relacionados con ayuda y compañerismo en el texto.
    
    Args:
        texto (str): Texto a analizar.
    
    Returns:
        list: Lista de términos relacionados con ayuda y compañerismo.
    """
    palabras_clave_ayuda = ['ayuda', 'solidaridad', 'compañerismo']
    return [palabra for palabra in palabras_clave_ayuda if palabra in texto]

# src/legal_processing.py

import openai

# Configura tu clave API de OpenAI
openai.api_key = 'sk-None-B6QFF6hAVv2tTz0yzAhST3BlbkFJeUFGBR95yyjz1AfohP2J'

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

