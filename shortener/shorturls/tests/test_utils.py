from unittest.mock import patch

from django.test import TestCase
from shorturls.utils import generate_short_url, generate_url_short_code


class UtilsTestCase(TestCase):
    def test_generate_url_short_code(self):
        code = generate_url_short_code()
        self.assertEqual(len(code), 8)

    @patch("shorturls.utils.settings")
    def test_generate_short_url_for_non_production(self, mocked_settings):
        mocked_settings.IS_PRODUCTION.return_value = False
        code = generate_url_short_code()
        short_url = generate_short_url(code)
        self.assertEqual(short_url, f"localhost:8000/{code}")

    @patch("shorturls.utils.settings")
    def test_generate_short_url_for_production(self, mocked_settings):
        mocked_settings.IS_PRODUCTION.return_value = True
        code = generate_url_short_code()
        short_url = generate_short_url(code)
        self.assertEqual(short_url, f"localhost:8000/{code}")
