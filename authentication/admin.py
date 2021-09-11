from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Skill, Experience, Education, Language, Project


class SkillsInline(admin.TabularInline):
    model = Skill
    extra = 0


class ExperiencesInLine(admin.TabularInline):
    model = Experience
    extra = 0


class EducationsInLine(admin.TabularInline):
    model = Education
    extra = 0


class LanguagesInLine(admin.TabularInline):
    model = Language
    extra = 0


class ProjectsInLine(admin.TabularInline):
    model = Project
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [SkillsInline, ExperiencesInLine, EducationsInLine, LanguagesInLine, ProjectsInLine]

    list_display = ('nome', 'email', 'is_staff', 'is_active')
    list_display_links = ('nome', 'email')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'password', 'email')
        }),
        ('Opções avançadas', {
            'classes': ('collapse',),
            'fields': (('is_staff', 'is_active'), 'is_superuser', 'groups', 'user_permissions'),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
