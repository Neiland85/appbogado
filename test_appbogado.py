import unittest
from app import app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def test_process_no_data(self):
        response = self.client.post('/process')
        self.assertEqual(response.status_code, 400)
        self.assertIn('No text provided', str(response.data))

    def test_process_with_data(self):
        response = self.client.post('/process', json={'text': 'Esto es una prueba.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('tokens', response.json)

    def test_process_invalid_json(self):
        response = self.client.post('/process', data='Invalid JSON')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
