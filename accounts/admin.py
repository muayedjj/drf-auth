from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ("Personal Info", {
            'fields': ('first_name', 'last_name', 'phone_number')
        })
    )


admin.site.register(CustomUser, CustomAdmin)
