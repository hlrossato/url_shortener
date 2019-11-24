from django.urls import path
from shorturls import views

app_name = "shorturls"
urlpatterns = [
    path("", views.UrlShortenerCreateView.as_view(), name="url-shortener"),
    path("search", views.UrlShortCodeSearchView.as_view(), name="short-code-search"),
    path(
        "<slug:url_short_code>",
        views.ShortUrlRedirectView.as_view(),
        name="short-url-detail",
    ),
]
