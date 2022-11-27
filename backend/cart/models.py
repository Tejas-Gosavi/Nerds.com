from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from comic.models import Comic
from core.settings import AUTH_USER_MODEL


class LoginCart(models.Model):
    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    comic = models.ManyToManyField(Comic, blank=True)
    count = models.IntegerField(blank=True, default=0)
    subtotal = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = _("Login Cart")
        verbose_name_plural = _("Login Cart")

    def __str__(self):
        return self.user.email


DELIVERY_STATUS_CHOICES = ((1, "Pending"), (2, "Delivered"), (3, "Failed"))
PAYMENT_STATUS_CHOICES = ((1, "Pending"), (2, "Done"), (3, "Failed"))


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.CharField(primary_key=True, max_length=100)
    order_slug = models.CharField(max_length=100, blank=True, null=True, unique=True)
    comic = models.ManyToManyField(Comic, blank=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    total = models.IntegerField(blank=True, default=0)
    delivery_charges = models.IntegerField(blank=True, default=10)
    delivery_status = models.IntegerField(
        blank=True, choices=DELIVERY_STATUS_CHOICES, default=1
    )
    payment_status = models.IntegerField(
        blank=True, choices=PAYMENT_STATUS_CHOICES, default=1
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.order_id

    def get_absolute_url(self):
        return reverse("cart:order_status", args={self.order_slug})
