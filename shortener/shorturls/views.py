from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, FormView
from shorturls.forms import UrlShortCodeForm, UrlShortenerForm
from shorturls.models import UrlShortener


class UrlShortenerCreateView(CreateView):
    form_class = UrlShortenerForm
    model = UrlShortener
    success_url = reverse_lazy("shorturls:url-shortener")
    template_name = "url_shortener_form.html"

    def form_valid(self, form):
        payload = {"long_url": form.cleaned_data.get("long_url")}
        self.object, _ = UrlShortener.objects.get_or_create(**payload)
        return render(self.request, self.template_name, {"object": self.object})


class UrlShortCodeSearchView(FormView):
    form_class = UrlShortCodeForm
    success_url = reverse_lazy("shorturls:short-code-search")
    template_name = "url_shortener_form.html"

    def form_valid(self, form):
        url_short_code = form.cleaned_data.get("url_short_code")

        try:
            self.object = UrlShortener.objects.get(url_short_code=url_short_code)
            context = {"object": self.object, "search": True}
        except UrlShortener.DoesNotExist:
            context = {"url_short_code": url_short_code}
            self.template_name = "not_found.html"

        return render(self.request, self.template_name, context)


class ShortUrlRedirectView(RedirectView):
    permanent = False
    pattern_name = "shorturls:short-url-detail"
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        shortened_url = get_object_or_404(
            UrlShortener, url_short_code=kwargs["url_short_code"]
        )
        self.url = shortened_url.long_url
        return super().get_redirect_url(*args, **kwargs)
