# appbogado/legal_processing.py

import spacy

nlp = spacy.load("es_core_news_md")

def leer_texto_legal(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

def procesar_texto_legal(texto):
    doc = nlp(texto)
    return doc

