# app.py

from flask import Flask, request, jsonify
from appbogado.legal_processing import leer_texto_legal, procesar_texto_legal
from appbogado.nlp_models import detectar_mentiras, identificar_difamaciones
from appbogado.defense_strategies import exigir_pruebas, destruir_argumento_insostenible

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.json
    texto = data.get('texto')
    
    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    
    doc = procesar_texto_legal(texto)
    mentiras = detectar_mentiras(texto)
    difamaciones = identificar_difamaciones(texto)
    respuesta = {
        'mentiras': mentiras,
        'difamaciones': difamaciones,
    }
    return jsonify(respuesta)

@app.route('/defensa', methods=['POST'])
def defensa():
    data = request.json
    acusacion = data.get('acusacion')
    
    if not acusacion:
        return jsonify({'error': 'No se proporcionó acusación'}), 400
    
    respuesta = {
        'exigir_pruebas': exigir_pruebas(acusacion),
        'destruir_argumento': destruir_argumento_insostenible(acusacion),
    }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)


