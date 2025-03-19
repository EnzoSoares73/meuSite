import os

from django.shortcuts import render

from blog.service import return_published_posts
from authentication.models import User


def landing(request):
    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except User.DoesNotExist:
        raise Exception("O sistema deve ter um usuário")

    context = {
        'user': user
    }

    return render(request, 'authentication/landing.html', context)


def home(request):
    num_blog_posts = 2
    lista_blog_posts = return_published_posts(request.LANGUAGE_CODE, num=num_blog_posts)

    for post in lista_blog_posts:
        post.text = truncate(post.text)

    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except User.DoesNotExist:
        raise Exception("O sistema deve ter um usuário")

    context = {
        'lista_blog_posts': lista_blog_posts,
        'user': user
    }

    return render(request, 'authentication/home.html', context)


def truncate(string, num_chars=200):
    if string != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&',
                         '<', '`',
                         '}', '.', '_', '=',
                         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        string = string[:num_chars]

        while string[-1] in special_chars:
            string = string[:-1]

        string += '...'

    return string
