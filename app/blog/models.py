from django.utils import timezone

from django.utils.translation import gettext as _, ngettext
from django.conf import settings

from django.db import models

from authentication.models import User

now = timezone.now()

def fixed_date():
    return timezone.now()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    pub_date = models.DateTimeField('Data de publicação', default=fixed_date)

    def __str__(self):
        return f'Post #{self.id}'

    def time_to_be_published(self):
        if self.pub_date > timezone.now():
            temp = self.pub_date - timezone.now()
            time_to_be_published = self.format_timedelta(temp)
            return _('Será publicado em %(time_to_be_published)s') % {
                'time_to_be_published': time_to_be_published}
        return _('Já publicado')

    @staticmethod
    def format_timedelta(timedeltatobeformatted):
        var = timedeltatobeformatted.total_seconds()

        days = var // (24 * 60 * 60)
        var -= days * (24 * 60 * 60)
        hours = var // (60 * 60)
        var -= hours * (60 * 60)
        minutes = var // 60

        string = ngettext("%(count_days)d dia", "%(count_days)d dias", int(days)) % {'count_days': int(days)}
        string += ', '

        string += ngettext("%(count_hours)d hora e", "%(count_hours)d horas e", int(hours)) % {
            'count_hours': int(hours)}

        string += ' '

        string += ngettext("%(count_minutes)d minuto", "%(count_minutes)d minutos", int(minutes)) % {
            'count_minutes': int(minutes)}

        return string


class Version(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Postagem')
    title = models.CharField('Título', max_length=50)
    subtitle = models.CharField('Subtítulo', max_length=50, null=True, blank=True)
    text = models.TextField('Texto')
    language_code = models.CharField('Código de Linguagem', max_length=5, choices=settings.LANGUAGES)

    class Meta:
        unique_together = ["post", "language_code"]
        verbose_name = "Versão"
        verbose_name_plural = "Versões"

    def __str__(self):
        return self.title
