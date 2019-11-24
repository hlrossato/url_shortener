from django.contrib import admin

from .models import UrlShortener


@admin.register(UrlShortener)
class UrlShortenerAdmin(admin.ModelAdmin):
    """Admin View for UrlShortener"""

    list_display = ("long_url", "short_url", "url_short_code")
    ordering = ("-pk",)
