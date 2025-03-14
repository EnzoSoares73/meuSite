from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.TextField('Sobre', null=True, default='Uma descrição sobre mim')
    linkedin = models.CharField(max_length=50, null=True)
    github = models.CharField(max_length=50, null=True)
    ddd = models.CharField('DDD', max_length=2, null=True)
    cellphone = models.CharField('Número de telefone', max_length=10, null=True)
    cv = models.FileField('Currículo', upload_to='pdfs', null=True, blank=True)
    picture = models.ImageField('Foto', upload_to='images', null=True, blank=True)

    def __str__(self):
        if (self.first_name + ' ' + self.last_name) != ' ':
            return self.first_name + ' ' + self.last_name
        return self.username

    def nome(self):
        return self

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
