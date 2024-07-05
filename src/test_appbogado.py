# test_appbogado.py

import pytest
from appbogado.legal_processing import leer_texto_legal, procesar_texto_legal
from appbogado.nlp_models import detectar_mentiras, identificar_difamaciones
from appbogado.defense_strategies import exigir_pruebas, destruir_argumento_insostenible
from appbogado.evaluation_models import calcular_equidad_judicial, calcular_transparencia_judicial

def test_leer_texto_legal():
    texto = leer_texto_legal("sample_legal.txt")
    assert isinstance(texto, str)

def test_procesar_texto_legal():
    texto = "Este es un texto de prueba."
    doc = procesar_texto_legal(texto)
    assert doc is not None

def test_detectar_mentiras():
    texto = "Esto es una mentira."
    resultado = detectar_mentiras(texto)
    assert len(resultado) > 0

def test_identificar_difamaciones():
    texto = "Esto es difamación."
    resultado = identificar_difamaciones(texto)
    assert len(resultado) > 0

def test_exigir_pruebas():
    acusacion = "Usted es culpable de fraude."
    respuesta = exigir_pruebas(acusacion)
    assert "proporcione pruebas" in respuesta

def test_destruir_argumento_insostenible():
    acusacion = "Usted es culpable de fraude."
    respuesta = destruir_argumento_insostenible(acusacion)
    assert "carece de pruebas sólidas" in respuesta

def test_calcular_equidad_judicial():
    equidad = calcular_equidad_judicial(0.8, 0.9, 0.7, 2.0, 0.9)
    assert equidad > 0

def test_calcular_transparencia_judicial():
    transparencia = calcular_transparencia_judicial(0.8, 0.9, 0.7, 0.8, 0.9)
    assert transparencia > 0

