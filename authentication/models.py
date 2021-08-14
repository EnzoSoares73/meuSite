from urllib.parse import urlparse, parse_qs
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from authentication import validators

def get_sentinel_user():
    return User.generate_sentinel()

class User(AbstractUser):
    about = models.TextField("Sobre", null=True, default='Uma descrição sobre mim')
    linkedin = models.CharField(max_length=50, null=True, default='')
    facebook = models.CharField(max_length=50, null=True, default='')
    github = models.CharField(max_length=50, null=True, default='')
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

class Skill(models.Model):
    name = models.CharField("Nome", max_length=20)
    proficiency = models.IntegerField("proeficiência", validators=[validators.validate_range])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField("Nome da empresa", max_length=50)
    start_date = models.DateField("Data de começo", default=None)
    end_date = models.DateField("Data de desligamento", default=None, null=True, blank=True)
    position = models.CharField("Cargo", max_length=20)
    place = models.CharField("Localidade", max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField("Nome da instituição", max_length=50)
    start_date = models.DateField("Data de começo", default=None)
    end_date = models.DateField("Data de desligamento", default=None, null=True, blank=True)
    place = models.CharField("Localidade", max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField("Nome", max_length=20)
    proficiency = models.IntegerField("proeficiência", validators=[validators.validate_range])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField("Nome", max_length=60)
    link = models.URLField("Link", null=True)
    description = models.TextField("Descrição")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def extract_video_id(self, url):
        query = urlparse(url)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in {'www.youtube.com', 'youtube.com'}:
            if query.path == '/watch':
                return parse_qs(query.query)['v'][0]
            if query.path[:7] == '/watch/':
                return query.path.split('/')[1]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]