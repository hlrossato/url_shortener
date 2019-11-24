from django.db import models
from shorturls.utils import generate_short_url, generate_url_short_code


class UrlShortener(models.Model):

    long_url = models.URLField("Long URL", max_length=200, db_index=True)
    short_url = models.URLField("Short URL", max_length=200, blank=True)
    url_short_code = models.SlugField("URL Short Code", unique=True, db_index=True)

    class Meta:
        verbose_name = "URL Shortener"
        verbose_name_plural = "URL Shortener"

    def save(self, *args, **kwargs):
        code = generate_url_short_code()
        self.url_short_code = code
        self.short_url = generate_short_url(code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.short_url
