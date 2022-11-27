from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Brand, ComicType


def brands(request):
    return {
        "brands_list": Brand.objects.filter(brand_to_feature=True),
    }


def product_types(request):
    return {"comic_type_list": ComicType.objects.filter(comic_type_to_feature=True)}
