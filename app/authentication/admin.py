from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import UserForm
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email', 'is_staff', 'is_active')
    list_display_links = ('nome', 'email')

    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'), 'email', 'password', 'about', ('linkedin', 'github'), ('ddd', 'cellphone'))
        }),
        ('Opções avançadas', {
            'classes': ('collapse',),
            'fields': (('is_staff', 'is_active'), 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    form = UserForm


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
