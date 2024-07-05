# app.py

from flask import Flask, request, jsonify
from appbogado.legal_processing import leer_texto_legal, procesar_texto_legal
from appbogado.nlp_models import detectar_mentiras, identificar_difamaciones
from appbogado.defense_strategies import exigir_pruebas, destruir_argumento_insostenible
from appbogado.evaluation_models import calcular_equidad_judicial, calcular_transparencia_judicial

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

@app.route('/evaluar_equidad', methods=['POST'])
def evaluar_equidad():
    data = request.json
    imparcialidad = data.get('imparcialidad')
    acceso = data.get('acceso')
    consistencia = data.get('consistencia')
    tiempo = data.get('tiempo')
    derechos = data.get('derechos')
    
    if not (imparcialidad and acceso and consistencia and tiempo and derechos):
        return jsonify({'error': 'Faltan parámetros'}), 400
    
    equidad = calcular_equidad_judicial(imparcialidad, acceso, consistencia, tiempo, derechos)
    return jsonify({'equidad_judicial': equidad})

@app.route('/evaluar_transparencia', methods=['POST'])
def evaluar_transparencia():
    data = request.json
    acceso_info = data.get('acceso_info')
    justificacion = data.get('justificacion')
    publicacion = data.get('publicacion')
    independencia = data.get('independencia')
    rendicion = data.get('rendicion')
    
    if not (acceso_info and justificacion and publicacion and independencia and rendicion):
        return jsonify({'error': 'Faltan parámetros'}), 400
    
    transparencia = calcular_transparencia_judicial(acceso_info, justificacion, publicacion, independencia, rendicion)
    return jsonify({'transparencia_judicial': transparencia})

if __name__ == '__main__':
    app.run(debug=True)

