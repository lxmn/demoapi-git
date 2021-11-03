import unittest

from betamax import Betamax
from demoapi.app import app

with Betamax.configure() as config:
    config.cassette_library_dir = 'test/fixtures'

test_auth_token = 'MLth87eHvSAaCQ1vn7jTd0xA9Kapo5'


class TestCases(unittest.TestCase):
    def setUp(self):
        # Necessary to disable SSLify
        app.debug = True
        self.test_app = app.test_client()
        self.session = app.requests_session

    def test_health_endpoint(self):
        """Assert that the health endpoint works."""
        response = app.test_client().get('/health')
        self.assertEquals(response.data, ';-)')

    def test_root_endpoint(self):
        """Assert that the / endpoint correctly redirects to login.uber.com."""
        response = app.test_client().get('/')
        self.assertIn('login.uber.com', response.data)

    def test_submit_endpoint_failure(self):
        """Assert that the submit endpoint returns no code in the response."""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['access_token'] = test_auth_token
            with Betamax(app.requests_session).use_cassette('submit_failure'):
                response = client.get('/submit?code=not_a_code')
        self.assertIn('None', response.data)

    def test_products_endpoint_returns_success(self):
        """Assert that the products endpoint returns success.
        When a valid key is passed in.
        """
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['access_token'] = test_auth_token
            with Betamax(app.requests_session).use_cassette('products_success'):
                response = client.get('/products')
        self.assertIn('products', response.data)
        self.assertEquals(response.status_code, 200)
