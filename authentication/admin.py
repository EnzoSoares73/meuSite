from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Skill, Experience, Education, Language, Project


class SkillsInline(admin.StackedInline):
    model = Skill
    extra = 1


class ExperiencesInLine(admin.StackedInline):
    model = Experience
    extra = 1


class EducationsInLine(admin.StackedInline):
    model = Education
    extra = 1


class LanguagesInLine(admin.StackedInline):
    model = Language
    extra = 1


class ProjectsInLine(admin.StackedInline):
    model = Project
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [SkillsInline, ExperiencesInLine, EducationsInLine, LanguagesInLine, ProjectsInLine]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
