from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("add", views.cart_add, name="cart_add"),
    path("delete", views.cart_delete, name="cart_delete"),
    path("checkout", views.checkout, name="checkout"),
    path("pay", views.pay, name="pay"),
    path("paymentStatus", views.paymentStatus, name="payment_status"),
    path("order/<slug:order_slug>", views.orderStatus, name="order_status"),
    # path("order-pdf/<slug:order_slug>", views.order_PDF, name="order_pdf"),
]
