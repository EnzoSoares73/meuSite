import json
import os
import urllib.request
import urllib.parse

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from authentication.forms import EmailForm
from authentication.models import User
from blog.models import Post


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
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)

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


def about(request):
    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except User.DoesNotExist:
        raise Exception("O sistema deve ter um usuário")

    projects = user.project_set.all()
    educations = user.education_set.order_by('-start_date')
    experiences = user.experience_set.order_by('-start_date')

    for project in projects:
        if project.extract_video_id(project.link) is not None:
            project.link = project.extract_video_id(project.link)

    context = {
        'user': user,
        'projects': projects,
        'educations': educations,
        'experiences': experiences,
    }

    return render(request, 'authentication/about.html', context)


def truncate(string, num_chars=200):
    if string != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                         '}', '.', '_', '=',
                         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        string = string[:num_chars]

        while string[-1] in special_chars:
            string = string[:-1]

        string += '...'

    return string
