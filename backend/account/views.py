from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from cart.models import Order
from cart.myCart import Cart
from comic.models import Comic

from .forms import UserRegistrationForm
from .models import User
from .tokens import account_activation_token

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
def get_user(request):
    instance = User.objects.all().first()
    print(instance)
    data = UserSerializer(instance).data
    return Response(data)

def profile(request):

    # if user is authenticated then
    # if request.user.is_authenticated:

        # show his/her profile
        user = User.objects.get(email=str(request.user))
        comics = Comic.objects.filter(wishlist_by=request.user)
        orders = Order.objects.filter(user=request.user.id).order_by("-created")
        context = {
            "user": user,
            "wishlist": comics,
            "orders": orders,
        }
        return render(request, "profile.html", context=context)

    # else redirect to authentication
    # else:
    #     return redirect("account:authenticate")


def authentication(request):

    # if user is logged in then
    if request.user.is_authenticated:

        # redirect user to his/her profile
        return redirect("account:profile")

    # else go for authentication
    else:
        return render(request, "authenticate.html")

@api_view(['POST'])
def userLogin(request):

    # if user is logged in then
    # if request.user.is_authenticated:

    #     # redirect user to his/her profile
    #     return redirect("account:profile")

    # # else if user is not logged in
    # else:

    #     # if reuqest is an ajax request and method is POST then
    #     if request.is_ajax() and request.method == "POST":

            # get user email and password
            email = request.data.get("email")
            password = request.data.get("password")

            # get user object from database
            user = User.objects.filter(email=email)

            # if user not in database then
            if not user.exists():

                # don't log in and return 3
                return Response({"status": "Fail", "data": [], "msg": "Wrong Email", "code": 1})

            # else if user is in our database then
            else:

                user = User.objects.get(email=email)

                # if user is is_active then
                if user.is_active:

                    # authenticate user
                    user = authenticate(email=email, password=password)

                    # if user is none means password is wrong then
                    if user == None:

                        # don't log in and return 2
                        return Response({"status": "Fail", "data": [], "msg": "Wrong Password", "code": 2})

                    # if password is correct then
                    else:

                        # update cart, log in user and return 0
                        # cart = Cart(request)
                        # cart.add_after_login(user)
                        # login(request, user)
                        data = UserSerializer(user).data
                        return Response({"status": "Success", "data": data, "msg": "Logged in successfully", "code": 0})

                # if user is not active then
                else:

                    # Incase account is deleted or account activation failed then this case happens
                    # don't log in and return 1
                    return Response({"status": "Fail", "data": [], "msg": "Account is deleted or not activated", "code": 3})

        # # else redirect to authentication
        # else:
        #     return redirect("account:authenticate")


def logout_account(request):

    # if user is logged in then
    if request.user.is_authenticated:

        # if request is an ajax request and method is POST then
        if request.is_ajax() and request.method == "POST":

            # logout user from current session and return 0
            logout(request)
            return JsonResponse({"logOutCode": 0})

        # else redirect user to his/her profile
        return redirect("account:profile")

    # else redirect to authentication
    else:
        return redirect("account:authenticate")


def signup_account(request):

    # if user is logged in then
    if request.user.is_authenticated:

        # redirect user to his/her profile
        return redirect("account:profile")

    # else if user is not logged in then
    else:

        # if request is an ajax request and method is POST then
        if request.is_ajax() and request.method == "POST":

            # get email and both passwords
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            # if user is in our database then
            user = User.objects.filter(email=email)
            if user.exists():

                # don't signup and return 3
                return JsonResponse({"signUpCode": 3})

            # else if user is not in our database then
            else:

                # if both passwords don't match then don't signup and return 2
                if password1 != password2:
                    return JsonResponse({"signUpCode": 2})

                # else if both passwords match then
                else:

                    # create user registration/sign up form
                    user = UserRegistrationForm(request.POST)

                    # if form is valid then
                    if user.is_valid():

                        # save form/create/sign up user and create email confirmation email template
                        user.save()
                        temp_user = User.objects.get(email=request.POST.get("email"))
                        current_site = get_current_site(request)
                        subject = "Activate your account"
                        message = render_to_string(
                            "account_activation_email.html",
                            {
                                "user": user,
                                "domain": current_site.domain,
                                "uid": urlsafe_base64_encode(force_bytes(temp_user.id)),
                                "token": account_activation_token.make_token(temp_user),
                            },
                        )

                        # send email confirmation email to user and retun 0
                        temp_user.email_user(subject=subject, message=message)
                        return JsonResponse({"signUpCode": 0})

                    # else if form is not valid then don't signup and return 1
                    else:
                        return JsonResponse({"signUpCode": 1})

        # else redirect to authentication
        else:
            return redirect("account:authenticate")


def account_activate(request, uidb64, token):

    context = {"activation": False}

    # check if user is present or not in our database
    try:

        # get uid and then get user object from that uid
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    # any error occurs then
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):

        # set user obejct to none
        user = None

    # if user is present in our database and account activation code/token is correct then
    if user is not None and account_activation_token.check_token(user, token):

        # user account is activated, save user object
        user.is_active = True
        user.save()
        context["activation"] = True

        # show success message
        return render(request, "account_activation_status.html", context=context)

    # else show failed message
    else:
        return render(request, "account_activation_status.html", context=context)


def delete_account(request):

    # if user is logged in then
    if request.user.is_authenticated:

        # if request is an ajax request and method is POST then
        if request.is_ajax() and request.method == "POST":

            # get user object, deactivate its account, logout from current session and return 0
            user = User.objects.get(email=str(request.user))
            user.is_active = False
            user.save()
            logout(request)
            return JsonResponse({"deleteAccountCode": 0})

        # else return to authentication
        else:
            return redirect("account:authenticate")

    # else return to authentication
    else:
        return redirect("account:authenticate")

@api_view(['POST'])
def saveUserPersonalData(request):

    # if user is logged in then
    # if request.user.is_authenticated:

        # if request is an ajax request and method is POST then
        if request.method == "POST":
            email = request.data.get("email")
            user = User.objects.get(email=email)
            user.first_name = request.data.get("first_name")
            user.last_name = request.data.get("last_name")
            user.phone_number = request.data.get("phone_number")
            user.save()
            return Response({"status": "Success", "data": user.getPersonalData(), "msg": "", "code": 0})
        else:
            
            # get user obejct, save/upadte old personal data with new, save user object and return 0
            # user = User.objects.get(email=str(request.user))
            # user.first_name = request.POST.get("firstName")
            # user.last_name = request.POST.get("lastName")
            # user.phone_number = request.POST.get("phoneNumber")
            # user.save()
            return Response({"status": "Fail", "data": [], "msg": "Wrong HTTP Method", "code": 1})

        # else return to authentication
        # else:
        #     return redirect("account:authenticate")

    # else return to authentication
    # else:
    #     return redirect("account:authenticate")

@api_view(['POST'])
def saveUserAddress(request):

    # if user is logged in then
    # if request.user.is_authenticated:

        # if request is an ajax request and method is POST then
        if request.method == "POST":

            # get user object, update old address fields with new, save user obejct and return 0
            email = request.data.get("email")
            user = User.objects.get(email=email)
            user.building_name = request.data.get("building_name")
            user.street_name = request.data.get("street_name")
            user.landmark = request.data.get("landmark")
            user.town_city = request.data.get("town_city")
            user.state = request.data.get("state")
            user.district = request.data.get("district")
            user.save()
            return Response({"status": "Success", "data": user.getAddress(), "msg": "", "code": 0})

        # else return to authentication
        else:
            return Response({"status": "Fail", "data": [], "msg": "Wrong HTTP Method", "code": 1})

    # else return to authentication
    # else:
    #     return redirect("account:authenticate")

def save_changePassword(request):

    # if user is logged in then
    if request.user.is_authenticated:

        # if request is an ajax request and method is POST then
        if request.is_ajax() and request.method == "POST":

            # create password change form
            form = PasswordChangeForm(request.user, request.POST)

            # if form is valid then
            if form.is_valid():

                # save form/update old password with new and return 0
                form.save()
                return JsonResponse({"changePasswordCode": 0})

            # else form is not valid then
            else:

                # if old password is incorrect then return 1
                if form.has_error(field="old_password", code="password_incorrect"):
                    return JsonResponse({"changePasswordCode": 1})

                # else if new password is similar to username then return 2
                elif form.has_error(field="new_password2", code="password_too_similar"):
                    return JsonResponse({"changePasswordCode": 2})

                # else if new password is too short/less than 8 characters then return 3
                elif form.has_error(field="new_password2", code="password_too_short"):
                    return JsonResponse({"changePasswordCode": 3})

                # else both passwords don't match and return 4
                else:
                    return JsonResponse({"changePasswordCode": 4})

        # else return to authentication
        else:
            return redirect("account:authenticate")

    # else return to authentication
    else:
        return redirect("account:authenticate")