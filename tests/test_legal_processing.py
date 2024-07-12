import unittest
from legal_processing import procesar_texto_legal

class TestLegalProcessing(unittest.TestCase):

    def setUp(self):
        self.texto_con_articulo = "Artículo 1. Todos los seres humanos nacen libres e iguales."
        self.texto_sin_articulo = "Todos los seres humanos nacen libres e iguales."

    def test_procesar_texto_legal(self):
        resultado = procesar_texto_legal(self.texto_con_articulo)
        esperado = {
            'articulo': 1,
            'contenido': 'Todos los seres humanos nacen libres e iguales.'
        }
        self.assertEqual(resultado, esperado)

    def test_procesar_texto_legal_sin_articulo(self):
        resultado = procesar_texto_legal(self.texto_sin_articulo)
        esperado = None
        self.assertEqual(resultado, esperado)

    def test_procesar_texto_legal_articulo_invalido(self):
        texto = "Artículo X. Todos los seres humanos nacen libres e iguales."
        resultado = procesar_texto_legal(texto)
        esperado = None
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()

