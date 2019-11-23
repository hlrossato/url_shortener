from django.test import TestCase
from django.urls import reverse
from shorturls.tests.mixins import UrlShortenerTestCaseMixin


class ShortUrlCreateViewTestCase(UrlShortenerTestCaseMixin, TestCase):
    def test_url_can_be_created(self):
        payload = {"long_url": self.long_url}
        response = self.client.post(reverse("shorturls:url-shortener"), payload)
        self.assertEqual(response.status_code, 200)
