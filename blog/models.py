from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta

class Post(models.Model):
    pub_date = models.DateTimeField("Data de publicação", default=datetime.now() + timedelta(hours=1))
    title = models.CharField("Título", max_length=50)
    text = models.TextField("Texto")

    def __str__(self):
        return self.title

    def time_to_be_published(self):
        if self.pub_date > datetime.now():
            return self.pub_date - datetime.now()
        else:
            return f"Já publicado em {self.pub_date}"
