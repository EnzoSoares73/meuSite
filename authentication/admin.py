from django.contrib import admin
from .models import User, Skill

class SkillsInline(admin.StackedInline):
    model = Skill
    extra = 3


class UserAdmin(admin.ModelAdmin):
    inlines = [SkillsInline]

admin.site.register(User, UserAdmin)
