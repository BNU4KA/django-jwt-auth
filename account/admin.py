from django.contrib import admin
from account.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "email", "is_admin", "role"]
    list_filter = ["is_admin", "role"]

    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username", "first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin", "role"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "first_name", "last_name", "password", "is_admin", "role"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(MyUser, UserAdmin)
