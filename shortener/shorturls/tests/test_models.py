from django.test import TestCase
from shorturls.models import UrlShortener
from shorturls.tests.mixins import UrlShortenerTestCaseMixin


class UrlShortenerTestCase(UrlShortenerTestCaseMixin, TestCase):
    def test_long_url_can_be_saved(self):
        """Ensure a long url can be saved (still without generate the
        short url version)
        """
        shortened_url = UrlShortener.objects.create(long_url=self.long_url)
        self.assertEqual(shortened_url.long_url, self.long_url)
        self.assertEqual(shortened_url.short_url, "")
        self.assertEqual(UrlShortener.objects.count(), 1)
        self.assertIsInstance(shortened_url, UrlShortener)
