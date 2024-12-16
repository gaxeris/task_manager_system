from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminUserCreationForm
from .models import User


class CustomUserCreationForm(AdminUserCreationForm):

    class Meta(AdminUserCreationForm.Meta):
        model = User
        fields = AdminUserCreationForm.Meta.fields + ("email",)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "email", "password1", "password2"),
                "classes": ("wide",),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
