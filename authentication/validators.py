from django.core.exceptions import ValidationError


def validate_range(value, min=0, max=100):
    if not (min <= value <= max):
        raise ValidationError(f"{value} não está entre {min} e {max}", params={'value': value})
    else:
        return value