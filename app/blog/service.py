from django.db.models import Prefetch
from django.utils import timezone

from .models import Post, Version

now = timezone.now()


def return_published_posts(lang, num=None):
    queryset = Post.objects.filter(pub_date__lt=now).order_by('-pub_date')
    if num is not None:
        queryset = queryset[:num]

    queryset = queryset.prefetch_related(
        Prefetch('version_set',
            queryset=Version.objects.filter(language_code=lang),
            to_attr='versions'
        ))

    translated_posts = []

    for post in queryset:
        if len(post.versions) == 0:
            continue
        version = post.versions[0]
        post.title = version.title
        post.text = version.text
        post.subtitle = version.subtitle
        translated_posts.append(post)

    return translated_posts
