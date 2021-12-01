import datetime

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    tag_title = models.CharField(max_length=50, blank=True)
    tag_slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("comic:comics_tag", args={self.tag_slug})

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.tag_title

class Talent(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = _("Creator")
        verbose_name_plural = _("Creators")

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_title = models.CharField(
        verbose_name=_("Brand Name"),
        help_text=_("Required and unique"),
        max_length=50,
        unique=True,
    )
    brand_slug = models.SlugField(
        verbose_name=_("Brand Slug"),
        help_text=_("Required and unique"),
        max_length=50,
        unique=True,
    )
    brand_to_feature = models.BooleanField(default=False)
    brand_is_active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("comic:comics_brand", args={self.brand_slug})

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.brand_title


class ComicType(models.Model):
    comic_type_title = models.CharField(
        verbose_name=_("Comic type Name"),
        help_text=_("Required and unique"),
        max_length=50,
        unique=True,
    )
    comic_type_slug = models.SlugField(
        verbose_name=_("Comic type Slug"),
        help_text=_("Required and unique"),
        max_length=50,
        unique=True,
    )
    comic_type_to_feature = models.BooleanField(default=False)
    comic_type_is_active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("comic:comics_type", args={self.comic_type_slug})

    class Meta:
        verbose_name = _("Comic Type")
        verbose_name_plural = _("Comic Types")

    def __str__(self):
        return self.comic_type_title


class Volume(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    volume_title = models.CharField(
        verbose_name=_("Volume/Series Name"),
        max_length=255,
    )
    volume_slug = models.SlugField(
        verbose_name=_("Volume/Series Slug"), max_length=50, unique=True
    )
    volume_start = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year),
        ],
    )
    volume_end = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year),
        ],
    )
    to_feature = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Volume/Series")
        verbose_name_plural = _("Volumes/Series")

    def get_absolute_url(self):
        return reverse("comic:comics_volume", args={self.volume_slug})

    def __str__(self):
        return self.volume_title


def comic_images_directory_path(instance, filename):
    fileExt = filename.split(".")[-1]
    return "/".join(
        [
            "images",
            instance.brand.brand_slug,
            instance.comic_type.comic_type_slug,
            instance.slug[:-2],
            instance.slug,
            instance.slug + "." + fileExt,
        ]
    )


AGE_RATING = (("13+", "13+"), ("15+", "15+"), ("18+", "18+"))


class Comic(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    comic_type = models.ForeignKey(ComicType, on_delete=models.CASCADE)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(
        verbose_name=_("Name"),
        max_length=50,
    )
    slug = models.SlugField(verbose_name=_("Slug"), max_length=50, unique=True)
    main_image = models.ImageField(upload_to=comic_images_directory_path, max_length=500)
    other_image1 = models.ImageField(upload_to=comic_images_directory_path, blank=True, max_length=500)
    other_image2 = models.ImageField(upload_to=comic_images_directory_path, blank=True, max_length=500)

    detail = models.TextField(blank=True)
    price = models.IntegerField()
    published_date = models.DateField(blank=True)
    
    written_by = models.ManyToManyField(Talent, blank=True, related_name="All_Writers")
    art_by = models.ManyToManyField(Talent, blank=True, related_name="All_Artists")
    page_count = models.IntegerField(blank=True)
    age_rating = models.CharField(max_length=5, choices=AGE_RATING, blank=True)

    wishlist_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    tags = models.ManyToManyField(Tag)

    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-published_date",)
        verbose_name = _("Comic")
        verbose_name_plural = _("Comics")

    def get_absolute_url(self):
        return reverse(
            "comic:comics_detail",
            kwargs={
                "brand_slug": self.brand.brand_slug,
                "comic_type_slug": self.comic_type.comic_type_slug,
                "slug": self.slug,
            },
        )

    def __str__(self):
        return self.title

class OneShot(Comic):
    class Meta:
        verbose_name = _("One Shot")
        verbose_name_plural = _("One Shot Issues")
