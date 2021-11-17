from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserEditForm, UserRegistrationForm
from .models import User


class User_Admin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserEditForm
    model = User

    list_display = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_active",
        "is_staff",
    )
    list_editable = ("is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    readonly_fields = (
        "id",
        "created",
        "updated",
        "is_active",
        "is_staff",
    )
    list_filter = ["is_active", "is_staff"]

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    filter_horizontal = ()
    fieldsets = ()
    ordering = ("email",)


admin.site.register(User, User_Admin)
