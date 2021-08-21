import json
import os
import urllib

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from authentication.forms import EmailForm
from authentication.models import User
from blog.models import Post


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
            if form.cleaned_data['email_dummy'] == form.emaildummy:
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': os.environ.get('RECAPTCHA_PRIVATE_KEY'),
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''

                if result['success']:
                    cd = form.cleaned_data
                    subject = "Sending an email with Django"
                    message = cd['message']
                    recipient = [os.environ.get("EMAIL")]
                    send_mail(subject, message,
                              settings.DEFAULT_FROM_EMAIL, recipient)
                    messageSent = True
                else:
                    messages.error(request, 'reCAPTCHA inválido.')
            else:
                messages.error(request, 'Comportamento suspeito encontrado')

    else:
        form = EmailForm()

    context = {
        'key': os.environ.get('RECAPTCHA_SITE_KEY'),
        'form': form,
        'messageSent': messageSent,
        'messages': messages.get_messages(request)
    }

    return render(request, 'authentication/contact.html', context)


def truncate(str, num_chars=384):
    if str != '':
        special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                         '}', '.', '_', '=',
                         ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '}

        str = str[:num_chars]

        while str[-1] in special_chars:
            str = str[:-1]

        str += '...'

    return str
