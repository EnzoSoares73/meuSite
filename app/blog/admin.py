from django.contrib import admin

from .forms import PostForm
from .models import Post, Version


class VersionInline(admin.StackedInline):
    model = Version
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [VersionInline]

    list_display = ('pub_date', 'time_to_be_published')

    fieldsets = (
        (None, {
            'fields': ('user', 'pub_date')
        }),
    )

admin.site.register(Post, PostAdmin)
