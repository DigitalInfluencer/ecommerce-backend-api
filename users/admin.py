from django.contrib import admin
from .models import User
from django.utils.html import format_html
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "provider",
        "is_active",
        "is_staff",
        "created_at",
        "avatar_preview",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "provider",
        "created_at",
    )

    search_fields = (
        "username",
        "email",
        "phone",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                obj.avatar.url
            )
        return "-"

    avatar_preview.short_description = "Avatar"