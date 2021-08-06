from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta, timezone

from authentication.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField("Data de publicação")
    title = models.CharField("Título", max_length=50)
    text = models.TextField("Texto")

    def __str__(self):
        return self.title

    def return_published_posts(self, num=None):
        lista_blog_posts = []
        for post in Post.objects.order_by('-pub_date'):
            if post.time_to_be_published() == "Já publicado":
                lista_blog_posts.append(post)
        if num is None:
            num = len(lista_blog_posts)
        return lista_blog_posts[:num]

    def time_to_be_published(self):
        if self.pub_date > datetime.now(timezone(timedelta(hours=-3))):
            temp = self.pub_date - datetime.now(timezone(timedelta(hours=-3)))
            str = self.format_timedelta(temp)
            return f"Será publicado em {str}"
        else:
            return "Já publicado"

    def format_timedelta(self, timedeltatobeformatted):
        var = timedeltatobeformatted.total_seconds()

        days = var // (24*60*60)
        var -= days * (24*60*60)
        hours = var // (60*60)
        var -= hours * (60*60)
        minutes = var // 60

        str = f"{int(days)}"

        if days == 1:
            str = str + " dia "
        else:
            str = str + " dias, "

        str = str+ f"{int(hours)}"

        if hours == 1:
            str = str + " hora "
        else:
            str = str + " horas e "

        str = str + f"{int(minutes)}"

        if minutes == 1:
            str = str + " minuto "
        else:
            str = str + " minutos"

        return str