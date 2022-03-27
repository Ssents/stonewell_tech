from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']
    fieldsets = (
        (None, 
            {'fields': ('email', 'username', 'password')}
        ),

        (_('Personal information'), 
            {
                'fields': ('first_name', 'last_name')
            }
        ),

        (_('Permissions'), 
            {
                'fields': ('is_active','is_staff')
            }
        ),

        (_('Important dates'),
            {
                'fields': ('joined_at',)
            }),
    )

admin.site.register(models.User, UserAdmin)