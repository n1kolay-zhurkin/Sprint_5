import random
import string


def generate_email():
    return f"test_testov_5_{random.randint(100, 999)}@yandex.ru"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))