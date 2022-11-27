from django.urls import include, path

from . import views

app_name = "account"

urlpatterns = [
    path("", views.profile, name="profile"),
    path("authenticate", views.authentication, name="authenticate"),
    path("login", views.login_account, name="login"),
    path("logout", views.logout_account, name="logout"),
    path("signup", views.signup_account, name="signup"),
    path(
        "activate/<slug:uidb64>/<slug:token>", views.account_activate, name="activate"
    ),
    path("delete", views.delete_account, name="delete"),
    path("save_perosnal_data", views.save_personalData, name="save_perosnal_data"),
    path(
        "save_change_password", views.save_changePassword, name="save_change_password"
    ),
    path(
        "save_shipping_address",
        views.save_shippingAddress,
        name="save_shipping_address",
    ),
]
