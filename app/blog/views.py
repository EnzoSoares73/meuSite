import markdown2
from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    lista_blog_posts = Post.return_published_posts()
    context = {
        'lista_blog_posts': lista_blog_posts
    }

    return render(request, 'blog/index.html', context)


def blog_post(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)

    blog.text = markdown2.markdown(blog.text, extras=['fenced-code-blocks'])
    context = {
        'blog': blog,
    }
    return render(request, 'blog/post.html', context)
