from django.core.exceptions import ValidationError


def validate_range(value, minimum=0, maximum=100):
    if not (minimum <= value <= maximum):
        raise ValidationError(f"{value} não está entre {minimum} e {maximum}", params={'value': value})
    return value
