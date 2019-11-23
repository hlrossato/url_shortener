import inspect
import os
import random
import string


def write_dot_env_file(env_file):
    settings = get_settings()
    with open(env_file, "w") as f:
        for k, v in settings.items():
            f.write(f"{k.upper()}={v}\n")


def get_settings():
    return {
        "SECRET_KEY": generate_secret_key(),
        "DEBUG": True,
        "DB_ENGINE": "django.db.backends.postgresql",
        "DB_USER": "postgres",
        "DB_PASSWORD": generate_password(),
        "DB_NAME": "postgres",
        "DB_PORT": "5432",
        "DB_HOST": "db",
        "ALLOWED_HOSTS": "*",
    }


def generate_secret_key():
    specials = "!@#$%^&*(-_=+)"
    chars = string.ascii_lowercase + string.digits + specials
    return "".join(random.choice(chars) for _ in range(50))


def generate_password():
    return generate_secret_key()[:16]


def set_debug():
    frame_info = inspect.stack()[1]
    filepath = frame_info[1]
    filename = os.path.basename(filepath)
    print("frame_info: ", frame_info)
    print("filepath: ", filepath)
    print("filename: ", filename)
    if "manage" in filename:
        return True
    return False


def dot_env_config():
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

    if not os.path.isfile(env_file):
        write_dot_env_file(env_file)
    else:
        pass
