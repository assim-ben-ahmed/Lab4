import unittest
from hello_world import app, generate_html, greet


class TestGenerateHTML(unittest.TestCase):
    """Test cases for the generate_html function"""
    
    def test_generate_html_structure(self):
        """Test that generate_html returns proper HTML structure"""
        message = "Hello World"
        result = generate_html(message)
        
        self.assertIn('<html>', result)
        self.assertIn('<body>', result)
        self.assertIn(message, result)
        self.assertIn('<image', result)
        self.assertIn('text-align:center', result)


class TestGreet(unittest.TestCase):
    """Test cases for the greet function"""
    
    def test_greet_returns_expected_message(self):
        """Test that greet returns the expected greeting message"""
        result = greet()
        expected = 'Welcome to CI/CD 101 using GitHub Actions!'
        self.assertEqual(result, expected)


class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask application"""
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_greeting_route_success(self):
        """Test that /greeting route works correctly"""
        response = self.client.get('/greeting')
        data = response.data.decode('utf-8')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn('Welcome to CI/CD 101 using GitHub Actions!', data)
    
    def test_nonexistent_route(self):
        """Test that non-existent routes return 404"""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
