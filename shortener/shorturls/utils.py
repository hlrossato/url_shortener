import random
import string

from django.conf import settings


def generate_url_short_code():
    alphabet = string.ascii_letters + string.digits
    return "".join(random.SystemRandom().choice(alphabet) for _ in range(8))


def generate_short_url(code):
    if not settings.IS_PRODUCTION:
        return f"localhost:8000/{code}"

    return f"localhost:8000/{code}"
