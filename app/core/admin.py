"""
Admin site for the school management system.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Admin page for the users."""
    ordering = ['id']
    list_filter = ['is_parent', 'is_staff', 'is_school_staff']
    list_display = ['email', 'is_school_staff', 'is_parent', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'),
         {
            'fields': (
                'is_staff',
                'is_school_staff',
                'is_parent',
                'is_superuser'
                )
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    # readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_school_staff',
                'is_parent',
                'is_superuser'

            )
        }),
    )

class StudentAdmin(admin.ModelAdmin):
    """Admin for the students."""
    list_display = ['name', 'student_id', 'current_class', 'join_date']
    ordering = ['current_class']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Staff)