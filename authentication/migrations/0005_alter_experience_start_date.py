# Generated by Django 3.2.6 on 2021-08-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0004_auto_20210813_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=None, null=True, verbose_name='Data de começo'),
        ),
    ]
