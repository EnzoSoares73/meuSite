import markdown2
from django.shortcuts import render, get_object_or_404

from .models import Post
from .service import return_published_posts


def index(request):
    lista_blog_posts = return_published_posts(request.LANGUAGE_CODE)
    context = {
        'lista_blog_posts': lista_blog_posts
    }

    return render(request, 'blog/index.html', context)


def blog_post(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    version = blog.version_set.all()[0]

    blog.text = markdown2.markdown(version.text, extras=['fenced-code-blocks'])
    blog.title = version.title
    blog.subtitle = version.subtitle

    context = {
        'blog': blog,
    }
    return render(request, 'blog/post.html', context)
