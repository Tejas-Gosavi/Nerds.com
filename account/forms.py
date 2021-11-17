from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
    forms,
)
from django.db import models

from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_password2(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            email = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email { email } already exists")


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        exclude = (
            "created",
            "updated",
            "last_login",
            "is_superuser",
            "groups",
            "user_permissions",
        )
        fields = "__all__"
