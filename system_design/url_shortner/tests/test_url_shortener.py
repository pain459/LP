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
        response = self.app.post('/', data=dict(
            original_url='https://example.com',
            short_name='example'
        ))
        self.assertEqual(response.status_code, 302)
        url = URL.query.filter_by(original_url='https://example.com').first()
        self.assertIsNotNone(url)
        self.assertEqual(url.short_name, 'example')

    def test_retrieve_url_by_hash(self):
        url_hash = 'testhash'
        url = URL(original_url='https://example.com', shortened_url='http://127.0.0.1:5000/testhash', url_hash=url_hash)
        with app.app_context():
            db.session.add(url)
            db.session.commit()

        response = self.app.get(f'/{url_hash}')
        self.assertEqual(response.status_code, 302)
        self.assertIn('https://example.com', response.location)

    def test_retrieve_url_by_short_name(self):
        short_name = 'example'
        url = URL(original_url='https://example.com', shortened_url='http://127.0.0.1:5000/testhash', url_hash='testhash', short_name=short_name)
        with app.app_context():
            db.session.add(url)
            db.session.commit()

        response = self.app.get(f'/s/{short_name}')
        self.assertEqual(response.status_code, 302)
        self.assertIn('https://example.com', response.location)

    def test_update_url(self):
        url = URL(original_url='https://example.com', shortened_url='http://127.0.0.1:5000/testhash', url_hash='testhash')
        with app.app_context():
            db.session.add(url)
            db.session.commit()

        response = self.app.post(f'/update/{url.id}', data=dict(
            new_original_url='https://newexample.com',
            short_name='newexample'
        ))
        self.assertEqual(response.status_code, 302)
        updated_url = URL.query.get(url.id)
        self.assertEqual(updated_url.original_url, 'https://newexample.com')
        self.assertEqual(updated_url.short_name, 'newexample')

    def test_delete_url(self):
        url = URL(original_url='https://example.com', shortened_url='http://127.0.0.1:5000/testhash', url_hash='testhash')
        with app.app_context():
            db.session.add(url)
            db.session.commit()

        response = self.app.post(f'/delete/{url.id}')
        self.assertEqual(response.status_code, 302)
        deleted_url = URL.query.get(url.id)
        self.assertIsNone(deleted_url)

if __name__ == '__main__':
    unittest.main()
