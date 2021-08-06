from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication import validators

class User(AbstractUser):
    about = models.TextField("Sobre")
    linkedin = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    ddd = models.CharField("DDD", max_length=2, null=True)
    cellphone = models.CharField("Número de telefone", max_length=10)
    cv = models.FileField("Currículo")
    picture = models.ImageField("Foto", upload_to="images")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Skill(models.Model):
    name = models.CharField("nome", max_length=20)
    proficiency = models.IntegerField("proeficiência", validators=[validators.validate_range])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
