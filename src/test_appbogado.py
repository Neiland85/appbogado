import unittest
from app import app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def post_request(self, endpoint, json_data):
        return self.client.post(endpoint, json=json_data)

    def test_process_no_data(self):
        response = self.post_request('/process', None)
        self.assertEqual(response.status_code, 400)
        self.assertIn('No se proporcionó texto', str(response.data))

    def test_process_with_data(self):
        response = self.post_request('/process', {'text': 'Esto es una prueba.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('tokens', response.json)

    def test_process_invalid_json(self):
        response = self.client.post('/process', data='Invalid JSON')
        self.assertEqual(response.status_code, 400)

    def test_detectar_emociones(self):
        response = self.post_request('/detectar_emociones', {'texto': 'Estoy muy feliz hoy.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('emociones', response.json)

    def test_clasificar_intenciones(self):
        response = self.post_request('/clasificar_intenciones', {'texto': 'Quiero aprender a programar.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('intenciones', response.json)

if __name__ == '__main__':
    unittest.main()
