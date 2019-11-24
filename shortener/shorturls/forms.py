import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from shorturls.models import UrlShortener


def validate_url_short_code(value):
    reg = re.compile(r"[a-zA-Z0-9]{8}")
    if not reg.match(value):
        raise ValidationError(f"{value} is an invalid URL short code")


class CrispyMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Go!"))


class UrlShortCodeForm(CrispyMixin, forms.Form):
    url_short_code = forms.SlugField(max_length=8, validators=[validate_url_short_code])


class UrlShortenerForm(CrispyMixin, forms.ModelForm):
    class Meta:
        model = UrlShortener
        fields = ("long_url",)
