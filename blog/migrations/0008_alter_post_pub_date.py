# Generated by Django 3.2.5 on 2021-07-30 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 23, 5, 3, 640577), verbose_name='Data de publicação'),
        ),
    ]
