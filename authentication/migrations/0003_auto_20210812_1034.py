# Generated by Django 3.2.6 on 2021-08-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210809_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cv',
            field=models.FileField(null=True, upload_to='pdfs', verbose_name='Currículo'),
        ),
    ]