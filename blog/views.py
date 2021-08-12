from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    num_blog_posts = 5
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)
    context = {
        'lista_blog_posts': lista_blog_posts
    }

    return render(request, 'blog/index.html', context)


def blog_post(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/post.html', context)
