import unittest
import server
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        self.app.testing = True 

    def test_home_endpoint(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, "Let's build a flight delay prediction api!")

    def test_predict_endpoint(self):
        response = self.app.get('/predict?airport_id=1&day_of_week=1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('model_prediction', data)
        self.assertIn('confidence_percent', data)
        self.assertIn('delayed_percent', data)
        self.assertIn('interpretation', data)

    def test_airports_endpoint(self):
        response = self.app.get('/airports')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('airports', data)

if __name__ == '__main__':
    unittest.main()