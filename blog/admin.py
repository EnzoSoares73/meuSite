from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'time_to_be_published')


admin.site.register(Post, PostAdmin)
