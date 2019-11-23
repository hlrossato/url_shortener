from django.db import models


class UrlShortener(models.Model):

    long_url = models.URLField("Long URL", max_length=200)
    short_url = models.URLField("Short URL", max_length=200, blank=True)

    class Meta:
        verbose_name = "URL Shortener"
        verbose_name_plural = "URL Shortener"

    def __str__(self):
        return self.short_url
