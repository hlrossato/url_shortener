import random
import string


def generate_url_short_code():
    alphabet = string.ascii_letters + string.digits
    return "".join(random.SystemRandom().choice(alphabet) for _ in range(8))


def generate_short_url(code):
    return f"http://localhost:8000/{code}"
