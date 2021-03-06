# Generated by Django 3.2.6 on 2021-08-14 02:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import authentication.validators


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0012_remove_education_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nome')),
                ('youtube_url', models.URLField(verbose_name='Link para YouTube')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
                ('proficiency', models.IntegerField(validators=[authentication.validators.validate_range],
                                                    verbose_name='proeficiência')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
