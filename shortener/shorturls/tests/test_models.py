from django.test import TestCase
from shorturls.models import UrlShortener
from shorturls.tests.mixins import UrlShortenerTestCaseMixin


class UrlShortenerTestCase(UrlShortenerTestCaseMixin, TestCase):
    def test_long_url_can_be_saved(self):
        """Ensure a long url can be saved correctly and the short url is
        generated
        """
        shortened_url = UrlShortener.objects.create(long_url=self.long_url)
        self.assertEqual(shortened_url.long_url, self.long_url)
        self.assertNotEqual(shortened_url.short_url, "")
        self.assertNotEqual(shortened_url.url_short_code, "")
        self.assertEqual(UrlShortener.objects.count(), 1)
        self.assertIsInstance(shortened_url, UrlShortener)
        self.assertEqual(shortened_url.__str__(), shortened_url.short_url)
