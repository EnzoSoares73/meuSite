# Generated by Django 3.2.5 on 2021-07-30 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(default='temp', max_length=10, verbose_name='Número de telefone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(default='temp', upload_to='', verbose_name='Currículo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='ddd',
            field=models.CharField(default='temp', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='temp', upload_to='images', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]