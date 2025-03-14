""" Cria um superusuário não-interativamente se ele não existir """

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Cria um superusuário não-interativamente se ele não existir
    através de create_superuser_if_not_exists
    """
    help = "Cria um superusuário não-interativamente se ele não existir"

    def handle(self, *args, **options):
        """ Lida com o comando """
        User = get_user_model()
        try:
            User.objects.get(username=os.environ.get('USER'))
        except User.DoesNotExist:
            User.objects.create_superuser(username=os.environ.get('USER'),
                                          email=os.environ.get('EMAIL'),
                                          password=os.environ.get('PASSWORD'))
