from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomAccountManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    # Delivery details
    phone_number = models.CharField(max_length=10, blank=True)
    building_name = models.CharField(max_length=150, blank=True)
    street_name = models.CharField(max_length=150, blank=True)
    landmark = models.CharField(max_length=50, blank=True)
    town_city = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)

    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"
        ordering = ("email",)

    def __str__(self):
        return self.email

    def email_user(self, subject, message):
        send_mail(
            subject=subject,
            message="",
            html_message=message,
            fail_silently=False,
            recipient_list=[self.email],
            from_email=settings.EMAIL_HOST_USER,
        )

    def can_order(self):
        if (
            self.first_name == ""
            or self.last_name == ""
            or self.phone_number == ""
            or self.building_name == ""
            or self.street_name == ""
            or self.landmark == ""
            or self.town_city == ""
            or self.district == ""
            or self.state == ""
        ):
            return False
        else:
            return True
