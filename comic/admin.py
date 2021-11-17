from django.contrib import admin

from .models import Annual, Brand, Comic, ComicType, Individual, Single, Tag, Volume


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tag_title", "tag_slug")
    prepopulated_fields = {"tag_slug": ("tag_title",)}
    search_fields = ("tag_title",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_title", "brand_slug", "brand_to_feature", "brand_is_active")
    list_editable = ("brand_to_feature", "brand_is_active")
    list_filter = ("brand_to_feature", "brand_is_active")
    prepopulated_fields = {"brand_slug": ("brand_title",)}
    search_fields = ("brand_title",)


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ("title", "comic_type", "brand", "price", "in_stock", "is_active")
    list_editable = ("in_stock", "is_active")
    list_filter = ("in_stock", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(ComicType)
class ComicTypeAdmin(admin.ModelAdmin):
    list_display = (
        "comic_type_title",
        "comic_type_slug",
        "comic_type_to_feature",
        "comic_type_is_active",
    )
    list_editable = ("comic_type_to_feature", "comic_type_is_active")
    list_filter = ("comic_type_to_feature", "comic_type_is_active")
    prepopulated_fields = {"comic_type_slug": ("comic_type_title",)}
    search_fields = ("comic_type_title",)


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = (
        "volume_title",
        "volume_slug",
        "brand",
        "volume_start",
        "volume_end",
        "to_feature",
        "is_active",
    )
    list_editable = ("to_feature", "is_active")
    list_filter = ("to_feature", "is_active")
    prepopulated_fields = {"volume_slug": ("volume_title",)}
    search_fields = ("volume_title",)


@admin.register(Single)
class SingleAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "volume", "price", "in_stock", "is_active")
    list_editable = ("in_stock", "is_active")
    list_filter = ("in_stock", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "published_date",
        "price",
        "in_stock",
        "is_active",
    )
    list_editable = ("in_stock", "is_active")
    list_filter = ("in_stock", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "published_date", "brand")


@admin.register(Annual)
class AnnualAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "published_date",
        "price",
        "in_stock",
        "is_active",
    )
    list_editable = ("in_stock", "is_active")
    list_filter = ("in_stock", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "published_date", "brand")
