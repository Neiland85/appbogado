import spacy

# Cargar el modelo de idioma
nlp = spacy.load("es_core_news_md")

def identificar_difamaciones(texto):
    doc = nlp(texto)
    difamaciones_detectadas = []
    for token in doc:
        if token.lower_ in ["difamación", "calumnia", "injuria"]:
            difamaciones_detectadas.append(token.text)
    return difamaciones_detectadas

def detectar_mentiras(texto):
    doc = nlp(texto)
    mentiras_detectadas = []
    for token in doc:
        if token.lower_ in ["mentira", "falso"]:
            mentiras_detectadas.append(token.text)
    return mentiras_detectadas

def exigir_pruebas(acusaciones):
    pruebas_exigidas = []
    for acusacion in acusaciones:
        pruebas_exigidas.append(f"Exigir prueba para: {acusacion}")
    return pruebas_exigidas

def destruir_argumentos(argumentos):
    argumentos_destruidos = []
    for argumento in argumentos:
        argumentos_destruidos.append(f"Destruido: {argumento}")
    return argumentos_destruidos

# Prueba de las funciones
if __name__ == "__main__":
    texto = "Este es un ejemplo de difamación y calumnia. Además, es una mentira y es falso."
    acusaciones = ["acusación 1", "acusación 2"]
    argumentos = ["argumento insostenible 1", "argumento insostenible 2"]

    print("Difamaciones detectadas:", identificar_difamaciones(texto))
    print("Mentiras detectadas:", detectar_mentiras(texto))
    print("Pruebas exigidas:", exigir_pruebas(acusaciones))
    print("Argumentos destruidos:", destruir_argumentos(argumentos))

