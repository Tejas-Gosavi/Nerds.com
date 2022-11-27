from django.shortcuts import get_list_or_404, get_object_or_404, render

from .myCart import Cart


def cart(request):
    return {
        "cart": Cart(request),
    }
