from django.shortcuts import render, get_object_or_404

from .models import Post

def append_strings_in_list(list):
    result = ''
    for string in list:
        result += str(string)
    return result


def taggify_start(content):
    text = f'<{content[0]}'
    if content[1] != '':
        text += f' class="{content[1]}">'
    else:
        text += '>'
    return text


def taggify_end(text):
    return '</' + text + '>'


def markdown_converter(text):
    signals = {
        'subsubtitle_signal': {
            '###': {
                'h3': ''
            }
        },
        'subtitle_signal': {
            '##': {
                'h2': ''
            }
        },
        'title_signal': {
            '#': {
                'h1': ''
            }
        },
        'code_signal': {
            '`': {
                'pre': 'container',
                'code': 'language-python code'
            }
        },
        'bold_signal': {
            '//': {
                'b': ''
            }
        },
    }

    for key, value in signals.items():
        for key1, value1 in value.items():
            var = True
            while (var):
                holder = text
                text = text.replace(key1, append_strings_in_list([taggify_start(j) for j in value1.items()]), 1)
                text = text.replace(key1, append_strings_in_list(reversed([taggify_end(j[0]) for j in value1.items()])), 1)
                if (holder == text):
                    var = False
    return text

def index(request):
    lista_blog_posts = Post.return_published_posts()
    context = {
        'lista_blog_posts': lista_blog_posts
    }

    return render(request, 'blog/index.html', context)


def blog_post(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    blog.text = markdown_converter(blog.text)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/post.html', context)
