# Generated by Django 3.2.6 on 2021-08-09 03:33

import blog.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=blog.models.fixed_date, null=True, verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='', null=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='Anonymous', null=True, on_delete=models.SET(blog.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]