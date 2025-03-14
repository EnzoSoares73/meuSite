from django.contrib import admin

from .forms import PostForm
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'time_to_be_published')

    fieldsets = (
        (None, {
            'fields': ('user', 'pub_date')
        }),
        ('Texto', {
            'fields': ['title', 'subtitle', 'text']
        }),
    )

    form = PostForm

admin.site.register(Post, PostAdmin)
