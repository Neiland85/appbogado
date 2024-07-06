import unittest
from appbogado import detectar_idiomas, extraer_argumentos

class TestAppbogado(unittest.TestCase):

    def test_detectar_idiomas(self):
        textos = ['es un texto', 'this is a text']
        result = detectar_idiomas(textos)
        self.assertEqual(result, ['español', 'inglés'])

    def test_extraer_argumentos(self):
        textos = ['es un texto', 'this is a text']
        result = extraer_argumentos(textos)
        expected = [{'texto': 'es un texto', 'argumento': 'simulado'}, {'texto': 'this is a text', 'argumento': 'simulado'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
