from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth.models import Group

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ['id', 'email', 'first_name', 'last_name']
    # search_fields = ('email',)
    ordering = ('first_name',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'token')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'token'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)