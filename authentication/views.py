from django.shortcuts import render

from blog.models import Post
from authentication.models import User


def home(request):
    num_blog_posts = 5
    lista_blog_posts = Post.objects.order_by('-pub_date')[:num_blog_posts]
    user = User.objects.get(username="EnzoSoares")
    context = {
        'lista_blog_posts': lista_blog_posts,
        'user': user,
    }

    return render(request, 'authentication/home.html', context)
