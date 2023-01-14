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
    phone_number = models.CharField(max_length=10, blank=True)

    # Delivery details
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

    def getPersonalData(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }
    
    def setPersonalData(self, obj):
        print(self, obj)
        self.first_name = obj.first_name
        self.last_name = obj.last_name
        self.phone_number = obj.phone_number
        self.save(self)
        
    def getAddress(self):
        return {
            "building_name": self.building_name,
            "street_name": self.street_name,
            "landmark": self.landmark,
            "town_city": self.town_city,
            "district": self.district,
            "state": self.state,
        }

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
