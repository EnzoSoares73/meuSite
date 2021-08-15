import os

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from authentication.forms import EmailForm
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

    projects = user.project_set.all()
    educations = user.education_set.order_by('-start_date')
    experiences = user.experience_set.order_by('-start_date')

    for project in projects:
        if (project.extract_video_id(project.link) != None):
            project.link = project.extract_video_id(project.link)


    context = {
        'user': user,
        'projects': projects,
        'educations': educations,
        'experiences': experiences,
    }

    return render(request, 'authentication/about.html', context)

def contact(request):

    messageSent = False

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']
            recipient = [os.environ.get("EMAIL")]

            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, recipient)

            messageSent = True

    else:
        form = EmailForm()

    context = {
        'form': form,
        'messageSent': messageSent,
    }

    return render(request, 'authentication/contact.html', context)

def truncate(str, num_chars = 384):
    if str != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=',
         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        str = str[:num_chars]

        while str[-1] in special_chars:
            str = str[:-1]

        str += '...'

    return str
