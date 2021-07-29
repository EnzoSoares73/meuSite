from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    welcome_msg = "Olá, você está na página inicial do blog\n"
    num_blog_posts = 5
    lista_blog_posts = Post.objects.order_by('-pub_date')[:num_blog_posts]
    context = {
        'lista_blog_posts': lista_blog_posts,
        'welcome_msg': welcome_msg,
    }

    return render(request, 'blog/index.html', context)


def blog_post(request, post_id):
    temp = get_object_or_404(Post, pk=post_id)
    context = {
        'title': temp.title,
        'text': temp.text,
    }
    return render(request, 'blog/post.html', context)
