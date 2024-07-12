from flask import Flask, request, jsonify
from appbogado.legal_processing import (
    leer_texto_legal, procesar_texto_legal, limpiar_texto, 
    identificar_entidades, detectar_sentencias_clave, analizar_sentimiento,
    detectar_anomalias, detectar_difamacion, detectar_ayuda_y_compañerismo
)
from appbogado.nlp_models import (
    detectar_mentiras, identificar_difamaciones, clasificar_texto,
    detectar_emociones, clasificar_intenciones, extraer_resumen, generar_respuesta
)
from appbogado.defense_strategies import exigir_pruebas, destruir_argumento_insostenible
from appbogado.evaluation_models import calcular_equidad_judicial, calcular_transparencia_judicial
from appbogado.audio_utils import AudioHandler

app = Flask(__name__)
audio_handler = AudioHandler()

def handle_request(route_function):
    def wrapper():
        data = request.json
        texto = data.get('texto')
        
        if not texto:
            return jsonify({'error': 'No se proporcionó texto'}), 400
        
        return route_function(texto)
    return wrapper

@app.route('/procesar', methods=['POST'])
@handle_request
def procesar(texto):
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

@app.route('/detectar_emociones', methods=['POST'])
@handle_request
def detectar_emociones_route(texto):
    emociones = detectar_emociones(texto)
    return jsonify({'emociones': emociones})

@app.route('/clasificar_intenciones', methods=['POST'])
@handle_request
def clasificar_intenciones_route(texto):
    intenciones = clasificar_intenciones(texto)
    return jsonify({'intenciones': intenciones})

@app.route('/extraer_resumen', methods=['POST'])
@handle_request
def extraer_resumen_route(texto):
    resumen = extraer_resumen(texto)
    return jsonify({'resumen': resumen})

@app.route('/generar_respuesta', methods=['POST'])
@handle_request
def generar_respuesta_route(texto):
    respuesta = generar_respuesta(texto)
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
