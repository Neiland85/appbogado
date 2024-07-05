# test_appbogado.py (continuación)

def test_limpiar_texto():
    texto = "Este es un texto de prueba!! Con caracteres especiales... y espacios  en blanco."
    texto_limpio = limpiar_texto(texto)
    assert texto_limpio == "Este es un texto de prueba Con caracteres especiales y espacios en blanco"

def test_identificar_entidades():
    texto = "El juez Juan Pérez dictó sentencia en el caso de María López."
    doc = procesar_texto_legal(texto)
    entidades = identificar_entidades(doc)
    assert ('Juan Pérez', 'PER') in entidades
    assert ('María López', 'PER') in entidades

def test_analizar_sentimiento():
    texto = "Este es un texto de prueba."
    sentimiento = analizar_sentimiento(texto)
    assert sentimiento is not None

def test_detectar_anomalias():
    texto = "Es imposible que esto haya sucedido. Nunca en la historia..."
    anomalías = detectar_anomalias(texto)
    assert "Declaración extrema detectada." in anomalías

def test_detectar_difamacion():
    texto = "Juan Pérez intentó difamar a su colega diciendo que es un ladrón."
    difamaciones = detectar_difamacion(texto)
    assert len(difamaciones) > 0

def test_detectar_ayuda_y_compañerismo():
    texto = "María siempre está dispuesta a ayudar y apoyar a sus colegas en momentos difíciles."
    ayuda = detectar_ayuda_y_compañerismo(texto)
    assert len(ayuda) > 0

