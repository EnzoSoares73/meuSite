#!/bin/bash

echo "Criando arquivos de tradução"
django-admin compilemessages

echo "Coletando arquivos estáticos"
python manage.py collectstatic --noinput

echo "Aplicando migrações"
python manage.py migrate

echo "Criando superusuário se ele não existir"
python manage.py create_superuser_if_not_exists

echo "Subindo aplicação"
python -m gunicorn meu_site.wsgi:application --bind 0.0.0.0:8000
