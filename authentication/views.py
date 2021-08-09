from django.shortcuts import render
from blog.models import Post
from authentication.models import User

def home(request):
    num_blog_posts = 2
    lista_blog_posts = Post.return_published_posts(num=num_blog_posts)
    post1 = lista_blog_posts[0]
    post1.text = truncate(post1.text)
    post2 = lista_blog_posts[1]
    post2.text = truncate(post2.text)
    user = User.objects.get(username="EnzoSoares")
    user.about = truncate(user.about)
    context = {
        'post1': post1,
        'post2': post2,
        'user': user
    }

    return render(request, 'authentication/home.html', context)

def truncate(str, num_chars = 384):
    special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=',
     ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

    str = str[:num_chars]

    while str[-1] in special_chars:
        str = str[:-1]

    str += '...'

    return str
