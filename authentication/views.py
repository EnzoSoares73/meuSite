from django.shortcuts import render

from blog.models import Post
from authentication.models import User


def home(request):
    num_blog_posts = 2
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)
    post1 = lista_blog_posts[0]
    post2 = lista_blog_posts[1]
    user = User.objects.get(username="EnzoSoares")
    context = {
        'post1': post1,
        'post2': post2,
        'user': user
    }

    return render(request, 'authentication/home.html', context)
