from flask import Flask, request, jsonify
from legal_processing import (
    leer_texto_legal, procesar_texto_legal, limpiar_texto, 
    identificar_entidades, detectar_sentencias_clave, analizar_sentimiento,
    detectar_anomalias, detectar_difamacion, detectar_ayuda_y_compañerismo
)
from nlp_models import (
    detectar_mentiras, identificar_difamaciones, clasificar_texto,
    detectar_emociones, clasificar_intenciones, extraer_resumen, generar_respuesta
)
from defense_strategies import (
    exigir_pruebas, destruir_argumento_insostenible, evaluar_solidez_argumento, construir_defensa
)
from evaluation_models import (
    calcular_equidad_judicial, calcular_transparencia_judicial
)

app = Flask(__name__)

# Helper function for handling JSON requests
def handle_request(route_function):
    def wrapper():
        data = request.json
        if not data:
            return jsonify({'error': 'No se proporcionaron datos'}), 400
        
        texto = data.get('texto')
        if not texto:
            return jsonify({'error': 'No se proporcionó texto'}), 400
        
        return route_function(texto, data)
    wrapper.__name__ = route_function.__name__ + "_wrapped"
    return wrapper

# Routes for legal_processing functions
@app.route('/procesar', methods=['POST'])
@handle_request
def procesar_route(texto, data):
    texto_limpio = limpiar_texto(texto)
    doc = procesar_texto_legal(texto_limpio)
    entidades = identificar_entidades(doc)
    sentimiento = analizar_sentimiento(texto_limpio)
    anomalías = detectar_anomalias(texto_limpio)
    difamaciones = detectar_difamacion(texto_limpio)
    ayuda = detectar_ayuda_y_compañerismo(texto_limpio)
    
    respuesta = {
        'entidades': entidades,
        'sentimiento': sentimiento,
        'anomalías': anomalías,
        'difamaciones': difamaciones,
        'ayuda': ayuda,
    }
    return jsonify(respuesta)

@app.route('/leer_texto_legal', methods=['POST'])
def leer_texto_legal_route():
    data = request.json
    ruta_archivo = data.get('ruta_archivo')
    
    if not ruta_archivo:
        return jsonify({'error': 'No se proporcionó la ruta del archivo'}), 400
    
    texto = leer_texto_legal(ruta_archivo)
    return jsonify({'texto': texto})

# Routes for nlp_models functions
@app.route('/detectar_mentiras', methods=['POST'])
@handle_request
def detectar_mentiras_route(texto, data):
    resultado = detectar_mentiras(texto)
    return jsonify({'resultado': resultado})

@app.route('/identificar_difamaciones', methods=['POST'])
@handle_request
def identificar_difamaciones_route(texto, data):
    resultado = identificar_difamaciones(texto)
    return jsonify({'difamaciones': resultado})

@app.route('/clasificar_texto', methods=['POST'])
@handle_request
def clasificar_texto_route(texto, data):
    resultado = clasificar_texto(texto)
    return jsonify({'clasificacion': resultado})

@app.route('/detectar_emociones', methods=['POST'])
@handle_request
def detectar_emociones_route(texto, data):
    emociones = detectar_emociones(texto)
    return jsonify({'emociones': emociones})

@app.route('/clasificar_intenciones', methods=['POST'])
@handle_request
def clasificar_intenciones_route(texto, data):
    intenciones = clasificar_intenciones(texto)
    return jsonify({'intenciones': intenciones})

@app.route('/extraer_resumen', methods=['POST'])
@handle_request
def extraer_resumen_route(texto, data):
    resumen = extraer_resumen(texto)
    return jsonify({'resumen': resumen})

@app.route('/generar_respuesta', methods=['POST'])
def generar_respuesta_route():
    data = request.json
    texto = data.get('texto')
    pregunta = data.get('pregunta')
    
    if not texto or not pregunta:
        return jsonify({'error': 'No se proporcionó texto o pregunta'}), 400
    
    respuesta = generar_respuesta(pregunta, texto)
    return jsonify({'respuesta': respuesta})

# Routes for defense_strategies functions
@app.route('/exigir_pruebas', methods=['POST'])
def exigir_pruebas_route():
    data = request.json
    afirmacion = data.get('afirmacion')
    
    if not afirmacion:
        return jsonify({'error': 'No se proporcionó afirmación'}), 400
    
    resultado = exigir_pruebas(afirmacion)
    return jsonify({'resultado': resultado})

@app.route('/destruir_argumento', methods=['POST'])
def destruir_argumento_route():
    data = request.json
    argumento = data.get('argumento')
    
    if not argumento:
        return jsonify({'error': 'No se proporcionó argumento'}), 400
    
    resultado = destruir_argumento_insostenible(argumento)
    return jsonify({'resultado': resultado})

@app.route('/evaluar_solidez', methods=['POST'])
def evaluar_solidez_route():
    data = request.json
    argumento = data.get('argumento')
    
    if not argumento:
        return jsonify({'error': 'No se proporcionó argumento'}), 400
    
    resultado = evaluar_solidez_argumento(argumento)
    return jsonify({'resultado': resultado})

@app.route('/construir_defensa', methods=['POST'])
def construir_defensa_route():
    data = request.json
    resultado = construir_defensa(data)
    return jsonify({'resultado': resultado})

# Routes for evaluation_models functions
@app.route('/calcular_equidad', methods=['POST'])
def calcular_equidad_route():
    data = request.json
    casos = data.get('casos')
    
    if not casos:
        return jsonify({'error': 'No se proporcionaron casos'}), 400
    
    resultado = calcular_equidad_judicial(casos)
    return jsonify({'equidad': resultado})

@app.route('/calcular_transparencia', methods=['POST'])
def calcular_transparencia_route():
    data = request.json
    casos = data.get('casos')
    
    if not casos:
        return jsonify({'error': 'No se proporcionaron casos'}), 400
    
    resultado = calcular_transparencia_judicial(casos)
    return jsonify({'transparencia': resultado})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

