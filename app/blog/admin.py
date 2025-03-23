from django.contrib import admin

from .models import Post, Version


class VersionInline(admin.StackedInline):
    model = Version
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [VersionInline]

    ordering = ['-pub_date']

    list_display = ('pub_date', 'time_to_be_published')

    fieldsets = (
        (None, {
            'fields': ('user', 'pub_date')
        }),
    )


admin.site.register(Post, PostAdmin)
