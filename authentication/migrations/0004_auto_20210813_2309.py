# Generated by Django 3.2.6 on 2021-08-14 02:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0003_auto_20210812_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome da empresa')),
                ('start_date', models.DateField(verbose_name='Data de começo')),
                ('end_date', models.DateField(verbose_name='Data de desligamento')),
                ('position', models.CharField(max_length=20, verbose_name='Cargo')),
                ('place', models.CharField(max_length=30, verbose_name='Localidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
