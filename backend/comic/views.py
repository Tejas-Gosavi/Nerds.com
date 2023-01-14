import django_filters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator

from .filters import ComicsFilter, VolumesFilter
from .models import Brand, Comic, ComicType, Tag, Volume

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def all_comics(request):
    data = {}

    # get all comics which are active/available and return them in context
    comics = Comic.objects.filter(is_active=True).values()
    # paginator_obj = Paginator(comics, 10)
    # current_page = request.data.get('pages', 1)

    # data["products"] = paginator_obj.get_page(current_page)
    # data["paginator"] = paginator_obj
    # data["current_page"] = int(current_page)
    data["comics"] = comics
    data["brands"] = Brand.objects.filter(brand_to_feature=True).values()
    data["comic_types"] = ComicType.objects.filter(comic_type_to_feature=True).values()
    return Response({"status": "Success", "data": data , "msg": "", "code": 0})

def all_volumes(request):
    context = {}

    # get all volumes which are active/available and return them in context
    volumes = Volume.objects.filter(is_active=True)

    # create filter/search based on request data
    volumes_filter = VolumesFilter(request.GET, queryset=volumes)

    # if no volumes present then
    if not volumes_filter.qs:

        # return 404 error page
        context["error"] = "Volumes you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        paginator_obj = Paginator(volumes_filter.qs, 5)
        current_page = request.GET.get('pages', 1)

        context["search_form"] = volumes_filter
        context["products"] = paginator_obj.get_page(current_page)
        context["paginator"] = paginator_obj
        context["current_page"] = int(current_page)
        return render(request, "volumes_search.html", context=context)


def comics_brand(request, brand_slug):
    context = {}

    # get all comics of respective brand, which are active/available
    comics = Comic.objects.filter(brand__brand_slug=brand_slug, is_active=True)

    # if no comics present of respective brand then
    if not comics:

        # return 404 error page
        context["error"] = "Brand you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        paginator_obj = Paginator(comics, 10)
        current_page = request.GET.get('pages', 1)

        context["products"] = paginator_obj.get_page(current_page)
        context["paginator"] = paginator_obj
        context["current_page"] = int(current_page)
        return render(request, "home.html", context=context)


def comics_type(request, comic_type_slug):
    context = {}

    # get all comics of respective comic type, which are active/available
    comics = Comic.objects.filter(
        comic_type__comic_type_slug=comic_type_slug, is_active=True
    )

    # if no comics present of respective comic type then
    if not comics:

        # return 404 error page
        context["error"] = "Comics with Comic type you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        paginator_obj = Paginator(comics, 10)
        current_page = request.GET.get('pages', 1)

        context["products"] = paginator_obj.get_page(current_page)
        context["paginator"] = paginator_obj
        context["current_page"] = int(current_page)
        return render(request, "home.html", context=context)


def comics_detail(request, **kwargs):
    context = {}

    # get comic of respetive brand, comic type, slug, which are active/available
    try:
        comic = Comic.objects.get(
            brand__brand_slug=kwargs.get("brand_slug"),
            comic_type__comic_type_slug=kwargs.get("comic_type_slug"),
            slug=kwargs.get("slug"),
            is_active=True,
        )

    # if no comic present / error occurs then
    except Comic.DoesNotExist:

        # return 404 error page
        context["error"] = "Comic you are requesting not found!"
        return render(request, "404.html", context=context)

    context["product"] = comic
    context["wishlisted"] = False

    # if user is logged in then
    if request.user.is_authenticated:

        # if given comic is wishlited by user then
        if comic.wishlist_by.filter(id=request.user.id).exists():
            context["wishlisted"] = True

    # if comic is part of volume/series then
    if comic.volume != None:

        # get volume/series info of that comic
        volume = Comic.objects.get(slug=kwargs.get("slug")).volume
        context["volume"] = volume

    # return them in context
    return render(request, "detail.html", context=context)


def comics_volume(request, volume_slug):
    context = {}

    # get all comics of respective volume, which are active/available
    comics = Comic.objects.filter(volume__volume_slug=volume_slug, is_active=True)

    # if no comics present of respective volume then
    if not comics:

        # return 404 error page
        context["error"] = "Volume you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        context["products"] = comics
        return render(request, "home.html", context=context)


def comics_search(request):
    context = {}

    # get all comics which are active/available
    comics = Comic.objects.filter(is_active=True)

    # create filter/search based on request data
    comics_filter = ComicsFilter(request.GET, queryset=comics)

    # if no comics are present in filter queryset then
    if not comics_filter.qs:

        # return 404 error page
        context["error"] = "Comics you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        paginator_obj = Paginator(comics_filter.qs, 3)
        current_page = request.GET.get('pages', 1)

        context["search"] = True
        context["search_form"] = comics_filter
        context["products"] = paginator_obj.get_page(current_page)
        context["paginator"] = paginator_obj
        context["current_page"] = int(current_page)
        return render(request, "search.html", context=context)


def comics_tag(request, tag_slug):
    context = {}

    # get all comics of respective tag, which are active/available
    comics = Comic.objects.filter(tags__tag_slug=tag_slug, is_active=True)

    # if no comics present of respective tag then
    if not comics:

        # return 404 error page
        context["error"] = "Comics with Tag you are requesting not found!"
        return render(request, "404.html", context=context)

    # else return them in context
    else:
        paginator_obj = Paginator(comics, 10)
        current_page = request.GET.get('pages', 1)

        context["products"] = paginator_obj.get_page(current_page)
        context["paginator"] = paginator_obj
        context["current_page"] = int(current_page)
        return render(request, "home.html", context=context)


def add_to_wishlist(request):
    context = {}

    # if user is logged in then
    if request.user.is_authenticated:

        # get comic of given id
        comic = get_object_or_404(Comic, id=request.POST.get("productId"))

        # if it is wishlisted then
        if comic.wishlist_by.filter(id=request.user.id).exists():

            # remove from wishlist and return 0
            comic.wishlist_by.remove(request.user)
            return JsonResponse({"toWishlistCode": 0})

        # else
        else:
            # add to wishlist and return 1
            comic.wishlist_by.add(request.user)
            return JsonResponse({"toWishlistCode": 1})

    # else return 2
    else:
        return JsonResponse({"toWishlistCode": 2})
