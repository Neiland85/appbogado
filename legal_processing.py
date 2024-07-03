# Código del archivo appbogado/legal_processing.py

import spacy
import re

nlp = spacy.load("es_core_news_md")

def leer_texto_legal(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

def procesar_texto_legal(texto):
    doc = nlp(texto)
    return doc

def limpiar_texto(texto):
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.strip()

def identificar_entidades(doc):
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades

def detectar_sentencias_clave(texto, palabras_clave):
    doc = nlp(texto)
    sentencias_clave = [sent.text for sent in doc.sents if any(palabra in sent.text for palabra in palabras_clave)]
    return sentencias_clave

def analizar_sentimiento(texto):
    doc = nlp(texto)
    sentimiento = doc._.polarity
    return sentimiento

def detectar_anomalias(texto):
    anomalías = []
    if "es imposible" in texto or "nunca" in texto:
        anomalías.append("Declaración extrema detectada.")
    return anomalías

def detectar_difamacion(texto):
    palabras_clave_difamacion = ['difamar', 'calumniar', 'injuriar']
    sentencias_difamacion = detectar_sentencias_clave(texto, palabras_clave_difamacion)
    return sentencias_difamacion

def detectar_ayuda_y_compañerismo(texto):
    palabras_clave_ayuda = ['ayudar', 'apoyar', 'colaborar']
    sentencias_ayuda = detectar_sentencias_clave(texto, palabras_clave_ayuda)
    return sentencias_ayuda

