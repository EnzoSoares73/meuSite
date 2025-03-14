#!/bin/bash

echo "Construindo migrações"
python manage.py makemigrations

echo "Aplicando migrações"
python manage.py migrate

echo "Criando superusuário se ele não existir"
python manage.py create_superuser_if_not_exists

echo "Subindo aplicação"
python manage.py runserver 0.0.0.0:8000