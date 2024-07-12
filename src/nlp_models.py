import spacy
from textblob import TextBlob
from transformers import pipeline

# Cargar modelo de spaCy
nlp = spacy.load('es_core_news_md')

# Cargar pipeline de Transformers para generación de respuestas y resumen
qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
summarization_pipeline = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')

def detectar_mentiras(texto):
    palabras_clave_mentira = ['no es cierto', 'falso', 'mentira']
    return any(palabra in texto for palabra in palabras_clave_mentira)

def identificar_difamaciones(texto):
    palabras_clave_difamacion = ['calumnia', 'difamación', 'injuria']
    return [palabra for palabra in palabras_clave_difamacion if palabra in texto]

def clasificar_texto(texto):
    if 'legal' in texto:
        return 'legal'
    elif 'personal' in texto:
        return 'personal'
    return 'otros'

def detectar_emociones(texto):
    analysis = TextBlob(texto)
    return analysis.sentiment_assessments.assessments

def clasificar_intenciones(texto):
    if 'quiero' in texto or 'necesito' in texto:
        return 'deseo'
    elif 'debería' in texto or 'tengo que' in texto:
        return 'obligación'
    return 'informativo'

def extraer_resumen(texto):
    summarized = summarization_pipeline(texto, max_length=50, min_length=25, do_sample=False)
    return summarized[0]['summary_text']

def generar_respuesta(pregunta, contexto):
    respuesta = qa_pipeline(question=pregunta, context=contexto)
    return respuesta['answer']
