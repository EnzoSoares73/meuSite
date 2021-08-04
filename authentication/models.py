from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    about = models.TextField("Sobre")
    linkedin = models.CharField(max_length=50)
    ddd = models.CharField("DDD", max_length=2)
    cellphone = models.CharField("Número de telefone", max_length=10)
    cv = models.FileField("Currículo")
    picture = models.ImageField("Foto", upload_to="images")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
