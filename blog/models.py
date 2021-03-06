from datetime import datetime, timedelta, timezone

from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.models import User


def fixed_date():
    return datetime.now(timezone(timedelta(hours=-3))) + timedelta(hours=1)


def get_sentinel_user():
    return User.generate_sentinel()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), null=True, default='Anonymous', verbose_name=User._meta.verbose_name)
    pub_date = models.DateTimeField('Data de publicação', null=True, default=fixed_date)
    title = models.CharField('Título', max_length=50, null=True, default='')
    text = models.TextField('Texto', null=True, default='')

    def __str__(self):
        return self.title

    @classmethod
    def return_published_posts(cls, num=None):
        lista_blog_posts = []
        for post in Post.objects.order_by('-pub_date'):
            if post.time_to_be_published() == 'Já publicado':
                lista_blog_posts.append(post)
        if num is None:
            num = len(lista_blog_posts)
        return lista_blog_posts[:num]

    def time_to_be_published(self):
        if self.pub_date > datetime.now(timezone(timedelta(hours=-3))):
            temp = self.pub_date - datetime.now(timezone(timedelta(hours=-3)))
            string = self.format_timedelta(temp)
            return f'Será publicado em {string}'
        return 'Já publicado'

    @staticmethod
    def format_timedelta(timedeltatobeformatted):
        var = timedeltatobeformatted.total_seconds()

        days = var // (24 * 60 * 60)
        var -= days * (24 * 60 * 60)
        hours = var // (60 * 60)
        var -= hours * (60 * 60)
        minutes = var // 60

        string = f'{int(days)}'

        if days == 1:
            string = string + ' dia '
        else:
            string = string + ' dias, '

        string = string + f'{int(hours)}'

        if hours == 1:
            string = string + ' hora '
        else:
            string = string + ' horas e '

        string = string + f'{int(minutes)}'

        if minutes == 1:
            string = string + ' minuto '
        else:
            string = string + ' minutos'

        return string
