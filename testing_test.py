import unittest
from errors import app  

class TestingTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        out = self.app.get('/')
        self.assertEqual(out.status, '200 OK')
        self.assertIn('charset=utf-8', out.content_type)
        self.assertIn('text/html', out.content_type)

if __name__ == "__main__":
    unittest.main()
