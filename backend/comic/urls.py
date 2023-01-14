from django.urls import include, path

from . import views

app_name = "comic"

urlpatterns = [
    path("", views.all_comics, name="all_comics"),
    # path("volumes", views.all_volumes, name="all_volumes"),
    # path("search", views.comics_search, name="comics_search"),
    # path("brand/<slug:brand_slug>", views.comics_brand, name="comics_brand"),
    # path("type/<slug:comic_type_slug>", views.comics_type, name="comics_type"),
    # path("volume/<slug:volume_slug>", views.comics_volume, name="comics_volume"),
    # path(
    #     "<slug:brand_slug>/<slug:comic_type_slug>/<slug:slug>",
    #     views.comics_detail,
    #     name="comics_detail",
    # ),
    # path("tag/<slug:tag_slug>", views.comics_tag, name="comics_tag"),
    # path("add-to-wishlist", views.add_to_wishlist, name="add_to_wishlist"),
]
