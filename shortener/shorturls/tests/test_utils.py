from django.test import TestCase
from shorturls.utils import generate_short_url, generate_url_short_code


class UtilsTestCase(TestCase):
    def test_generate_url_short_code(self):
        code = generate_url_short_code()
        self.assertEqual(len(code), 8)

    def test_generate_short_url(self):
        code = generate_url_short_code()
        short_url = generate_short_url(code)
        self.assertEqual(short_url, f"localhost:8000/{code}")
