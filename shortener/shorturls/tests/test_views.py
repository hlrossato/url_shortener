from django.test import TestCase
from django.urls import reverse
from shorturls.models import UrlShortener
from shorturls.tests.mixins import UrlShortenerTestCaseMixin


class ShortUrlCreateViewTestCase(UrlShortenerTestCaseMixin, TestCase):
    def test_url_can_be_created(self):
        payload = {"long_url": self.long_url}
        response = self.client.post(
            reverse("shorturls:url-shortener"), payload, follow=True
        )
        self.assertEqual(response.status_code, 200)

        obj = response.context.get("object")
        self.assertEqual(obj.long_url, self.long_url)
        self.assertEqual(len(obj.url_short_code), 8)


class UrlShortCodeSearchViewTestCase(UrlShortenerTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.shortened_url = UrlShortener.objects.create(long_url=self.long_url)

    def test_url_can_be_search_based_on_a_created_code(self):
        payload = {"url_short_code": self.shortened_url.url_short_code}
        response = self.client.post(reverse("shorturls:short-code-search"), payload)

        self.assertEqual(response.status_code, 200)
        obj = response.context.get("object")
        self.assertEqual(obj, self.shortened_url)
        self.assertIsInstance(obj, UrlShortener)

    def test_search_view_redirects_to_non_found_page(self):
        payload = {"url_short_code": "test1234"}
        response = self.client.post(reverse("shorturls:short-code-search"), payload)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context.get("object"))
        self.assertIn("url_short_code", response.context)
        self.assertEqual(
            response.context.get("url_short_code"), payload.get("url_short_code")
        )


class ShortUrlRedirectViewTestCase(UrlShortenerTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.shortened_url = UrlShortener.objects.create(long_url=self.long_url)

    def test_view_redirects_correctly(self):
        url = reverse(
            "shorturls:short-url-detail",
            kwargs={"url_short_code": self.shortened_url.url_short_code},
        )
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.shortened_url.long_url)

    def test_redirect_view_returns_404(self):
        url = reverse(
            "shorturls:short-url-detail", kwargs={"url_short_code": "test1234"}
        )
        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)
