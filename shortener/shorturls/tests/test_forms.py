from django.core.validators import ValidationError
from django.test import TestCase
from shorturls.forms import (UrlShortCodeForm, UrlShortenerForm,
                             validate_url_short_code)
from shorturls.utils import generate_url_short_code


class ShortURLFormsTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.code = generate_url_short_code()
        self.wrong_value = "Test"
        self.long_url = "https://google.com"

    def test_validate_url_short_code_raises_validation_error(self):
        with self.assertRaises(ValidationError):
            validate_url_short_code(self.wrong_value)

    def test_urlshortcodeform_valid(self):
        form = UrlShortCodeForm(data={"url_short_code": self.code})
        self.assertTrue(form.is_valid())

    def test_urlshortcodeform_invalid(self):
        form = UrlShortCodeForm(data={"url_short_code": self.wrong_value})
        self.assertFalse(form.is_valid())

    def test_UrlShortenerForm_valid(self):
        form = UrlShortenerForm(data={"long_url": self.long_url})
        self.assertTrue(form.is_valid())

    def test_UrlShortenerForm_invalid(self):
        form = UrlShortenerForm(data={"long_url": self.wrong_value})
        self.assertFalse(form.is_valid())
