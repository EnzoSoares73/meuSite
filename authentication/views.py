import os

from django.shortcuts import render
from blog.models import Post
from authentication.models import User, Skill


def home(request):
    num_blog_posts = 2
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)

    try:
        post1 = lista_blog_posts[0]
    except IndexError:
        post1 = Post.generate_sentinel()
    post1.text = truncate(post1.text)

    try:
        post2 = lista_blog_posts[1]
    except IndexError:
        post2 = Post.generate_sentinel()
    post2.text = truncate(post2.text)

    try:
        user = User.objects.get(username=os.environ.get("USER"))
    except:
        user = User.generate_sentinel()
    user.about = truncate(user.about)

    if user.skill_set.all().count() == 0:
        Skill.generate_sentinel()

    context = {
        'post1': post1,
        'post2': post2,
        'user': user
    }

    return render(request, 'authentication/home.html', context)

def truncate(str, num_chars = 384):
    if str != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=',
         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        str = str[:num_chars]

        while str[-1] in special_chars:
            str = str[:-1]

        str += '...'

    return str
