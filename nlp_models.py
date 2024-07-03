# appbogado/nlp_models.py

from transformers import pipeline

# Cargar modelos preentrenados
mentira_detector = pipeline("text-classification", model="mrm8488/bert-small-finetuned-covid19-spa-lies", tokenizer="mrm8488/bert-small-finetuned-covid19-spa-lies")
difamacion_detector = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sentiment-spanish", tokenizer="mrm8488/bert-tiny-finetuned-sentiment-spanish")

def detectar_mentiras(texto):
    resultado = mentira_detector(texto)
    return resultado

def identificar_difamaciones(texto):
    resultado = difamacion_detector(texto)
    return resultado


