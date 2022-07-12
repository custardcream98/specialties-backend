from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import users.models as userModels


@admin.register(userModels.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "wallet_address",
                )
            }
        ),
    )
