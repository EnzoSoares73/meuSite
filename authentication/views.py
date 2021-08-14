import os

from django.shortcuts import render
from blog.models import Post
from authentication.models import User, Skill


def home(request):
    num_blog_posts = 2
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)

    for post in lista_blog_posts:
        post.text = truncate(post.text)

    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except:
        user = User.generate_sentinel()

    context = {
        'lista_blog_posts': lista_blog_posts,
        'user': user
    }

    return render(request, 'authentication/home.html', context)

def about(request):
    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except:
        user = User.generate_sentinel()

    context = {
        'user': user,
    }

    return render(request, 'authentication/about.html', context)

def truncate(str, num_chars = 384):
    if str != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=',
         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        str = str[:num_chars]

        while str[-1] in special_chars:
            str = str[:-1]

        str += '...'

    return str
