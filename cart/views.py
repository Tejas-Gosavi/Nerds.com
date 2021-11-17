from io import BytesIO

import razorpay
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt

from account.models import User
from comic.models import Comic, ComicType

from .models import LoginCart, Order
from .myCart import Cart


def cart_add(request):

    # create current Cart object
    cart = Cart(request)

    # if request is an ajax request and method is GET then
    if request.is_ajax and request.method == "GET":

        # get comic id and comic from that comic id
        comicId = int(request.GET.get("productId"))
        comic = get_object_or_404(Comic, id=comicId)

        # if comic is added in cart then return 0
        if cart.add(comic, request.user.is_authenticated, request.user.id):
            return JsonResponse({"addToCartCode": 0})

        # else return 1
        else:
            return JsonResponse({"addToCartCode": 1})

    # else redirect to authentication
    else:
        return redirect("account:authenticate")


def cart_delete(request):

    # create current Cart object
    cart = Cart(request)

    # if request is an ajax request and method is GET then
    if request.is_ajax and request.method == "GET":

        # get comic id and comic from that comic id
        comicId = int(request.GET.get("productId"))
        comic = get_object_or_404(Comic, id=comicId)

        # if comic is removed from cart then return 0
        if cart.delete(comic, request.user.is_authenticated, request.user.id):
            return JsonResponse({"deleteFromCartCode": 0})

        # else return 1
        else:
            return JsonResponse({"deleteFromCartCode": 1})

    # else redirect to authentication
    else:
        return redirect("account:authenticate")


@login_required
def checkout(request):

    # get current user object
    user = User.objects.get(id=request.user.id)
    context = {
        "can_order": user.can_order(),  # return if he can order or not
    }
    return render(request, "checkout.html", context=context)


@login_required
def pay(request):

    context = {}

    # if request is an ajax request and method is GET then
    if request.method == "POST":

        # create order using Razorpay
        amount = int(request.POST["total"])
        delivery_charges = int(request.POST["deliveryOption"])
        client = razorpay.Client(
            auth=("rzp_test_l6Uqui0w9OG5Lh", "CrKebbX9r8AOR2ZzoRwpBCIc")
        )
        data = {"amount": amount * 100, "currency": "INR", "payment_capture": "1"}
        razorpayOrder = client.order.create(data=data)

        # get user cart and and id of comics present in my cart
        user = User.objects.get(id=request.user.id)
        myCart = LoginCart.objects.get(user=user)
        myCartItemsId = myCart.comic.all().values_list(flat=True)

        # create my order
        myOrder = Order.objects.create(
            user=user,
            order_id=razorpayOrder["id"],
            order_slug=slugify(razorpayOrder["id"]),
            total=amount,
            delivery_charges=delivery_charges,
            delivery_status=1,
            payment_status=1,
        )
        myOrder.comic.add(*myCartItemsId)
        myOrder.save()

        # clear my cart
        myCart.comic.clear()
        myCart.subtotal = 0
        myCart.count = 0
        myCart.save()

        # clear cart from sessions
        _ = request.session.pop("sessionKey")

        context = razorpayOrder
        context["callback_url"] = (
            "http://" + str(get_current_site(request)) + "/cart/paymentStatus"
        )
        return render(request, "pay.html", context=context)

    # else redirect to checkout
    else:
        return redirect("cart:checkout")


@csrf_exempt
@login_required
def orderStatus(request, order_slug):

    # get order obejct
    order = Order.objects.get(user=request.user.id, order_slug=order_slug)
    context = {
        "order": order,
    }
    return render(request, "orderStatus.html", context=context)


@csrf_exempt
@login_required
def paymentStatus(request):

    # get order_id, payment_id from request data
    order_id = request.POST["razorpay_order_id"]
    payment_id = request.POST["razorpay_payment_id"]

    # get order object and update payment id
    order = Order.objects.get(order_id=order_id)
    order.payment_id = payment_id

    # if error in request data then
    if "error" in request.POST:

        # order payment is failed
        order.PAYMENT_STATUS_CHOICES = 3
        order.save()
    else:

        # order payment is successed
        order.PAYMENT_STATUS_CHOICES = 2
        order.save()

        # email user about payment
        user = User.objects.get(id=order.user.id)
        subject = "Payment successfull"
        message = render_to_string(
            "paymentSuccess.html",
            {
                "user": user,
                "order": order,
            },
        )
        user.email_user(subject=subject, message=message)

        # redirect to order
        return redirect(order)


# Igonre code below


# def order_PDF(request, order_slug):
#     order = Order.objects.get(order_slug=order_slug)
#     user = User.objects.get(id=order.user_id)
#     context = {
#         "order": order,
#         "user": user,
#     }
#     return render(request, "orderPDF.html", context=context)

# def render_to_pdf(order_slug):
#     order = Order.objects.get(order_slug=order_slug)
#     user = User.objects.get(id=order.user_id)
#     context = {
#             'user': user,
#             'order': order,
#     }
#     template = get_template('/templates/orderPDF.html')
#     html = template.render(context)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
