# app.py (continuación)

from flask import Flask, request, jsonify
from appbogado.legal_processing import (
    leer_texto_legal, procesar_texto_legal, limpiar_texto, 
    identificar_entidades, detectar_sentencias_clave, analizar_sentimiento,
    detectar_anomalias, detectar_difamacion, detectar_ayuda_y_compañerismo
)
from appbogado.nlp_models import detectar_mentiras, identificar_difamaciones, clasificar_texto
from appbogado.defense_strategies import exigir_pruebas, destruir_argumento_insostenible
from appbogado.evaluation_models import calcular_equidad_judicial, calcular_transparencia_judicial
from appbogado.audio_utils import AudioHandler

app = Flask(__name__)
audio_handler = AudioHandler()

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.json
    texto = data.get('texto')
    
    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    
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

# Otras rutas existentes

if __name__ == '__main__':
    app.run(debug=True)

