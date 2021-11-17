from django.contrib import admin

from .models import LoginCart, Order


@admin.register(LoginCart)
class LoginCartAdmin(admin.ModelAdmin):
    list_display = ("user", "count", "subtotal")
    search_fields = ("user",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_id", "payment_id", "total", "delivery_charges")
    list_filter = ("delivery_status", "payment_status")
    prepopulated_fields = {"order_slug": ("order_id",)}
    search_fields = ("user",)
