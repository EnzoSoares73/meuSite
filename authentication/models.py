from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication import validators

def get_sentinel_user():
    return User.generate_sentinel()

class User(AbstractUser):
    about = models.TextField("Sobre", null=True, default='Uma descrição sobre mim')
    linkedin = models.CharField(max_length=50, null=True, default='')
    facebook = models.CharField(max_length=50, null=True, default='')
    ddd = models.CharField("DDD", max_length=2, null=True, default='')
    cellphone = models.CharField("Número de telefone", null=True, max_length=10, default='')
    cv = models.FileField("Currículo", upload_to="pdfs", null=True)
    picture = models.ImageField("Foto", upload_to="images", null=True)

    def __str__(self):
        if (self.first_name + ' ' + self.last_name) != ' ':
            return self.first_name + ' ' + self.last_name
        else:
            return self.username

    @classmethod
    def generate_sentinel(cls):
        return User.objects.get_or_create(username="Anonymous")[0]

    @classmethod
    def generate_placeholder(cls):
        return User(username="Anonymous")

class Skill(models.Model):
    name = models.CharField("nome", max_length=20)
    proficiency = models.IntegerField("proeficiência", validators=[validators.validate_range])
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))

    def __str__(self):
        return self.name

    @classmethod
    def generate_sentinel(cls):
        return Skill.objects.get_or_create(name="Sentinel",
                                           proficiency=50,
                                           user=User.generate_sentinel())[0]

    @classmethod
    def generate_placeholder(cls):
        return Skill(name="Sentinel",
                    proficiency=50,
                    user=User.generate_sentinel())
