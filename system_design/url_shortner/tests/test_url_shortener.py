import unittest
from app import app, db
from app.models import URL

class URLShortenerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_shorten_url(self):
        response = self.app.post('/shorten', json={'original_url': 'http://example.com'})
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertIn('shortened_url', data)

    def test_retrieve_url(self):
        self.app.post('/shorten', json={'original_url': 'http://example.com'})
        response = self.app.get('/' + 'http://example.com')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('original_url', data)

    def test_update_url(self):
        self.app.post('/shorten', json={'original_url': 'http://example.com'})
        response = self.app.put('/update/http://example.com', json={'original_url': 'http://newexample.com'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('shortened_url', data)

    def test_delete_url(self):
        self.app.post('/shorten', json={'original_url': 'http://example.com'})
        response = self.app.delete('/delete/http://example.com')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
