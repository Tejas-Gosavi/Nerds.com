from django.urls import include, path

from . import views

app_name = "account"

urlpatterns = [
    path("", views.profile, name="profile"),
    path("userLogin", views.userLogin, name="login"),
    # path("logout", views.logout_account, name="logout"),
    # path("signup", views.signup_account, name="signup"),
    # path(
    #     "activate/<slug:uidb64>/<slug:token>", views.account_activate, name="activate"
    # ),
    # path("delete", views.delete_account, name="delete"),
    path("saveUserPersonalData", views.saveUserPersonalData, name="save_perosnal_data"),
    path("saveUserAddress", views.saveUserAddress, name="save_shipping_address"),
    # path(
    #     "save_change_password", views.save_changePassword, name="save_change_password"
    # ),
    path('drf', views.get_user, name="get_user")
]
