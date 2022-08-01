from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering=["id"]
    list_display=["email", "name"]
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (_('Important dates'), {'fields': ('last_login',)}),)

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),)
    # fieldsts=(
    #     (None, {"fields":("email","password")}),
    #     (_("personal"), {"fields":("name",)}),
    #     (_("permissions"), {"fields":("is_avtive","is_staff" , "is_superuser")}),
    #     (_("important dates"), {"fields":("date_joined",)}),


        


    # )
  

    

admin.site.register(models.User, UserAdmin)