from django.contrib import admin

from authentication.models import User
from .models import Post


class UsersInline(admin.StackedInline):
    model = User
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'time_to_be_published')


admin.site.register(Post, PostAdmin)
