import django_filters
from django.forms import Textarea

from comic.models import Comic, Volume


class ComicsFilter(django_filters.FilterSet):
    class Meta:
        model = Comic
        fields = {
            "title": ["icontains"],
            "brand": ["exact"],
            "comic_type": ["exact"],
            "price": ["lte", "gte"],
        }


class VolumesFilter(django_filters.FilterSet):
    class Meta:
        model = Volume
        fields = {
            "volume_title": ["icontains"],
            "brand": ["exact"],
            "volume_start": ["gte"],
            "volume_end": ["lte"],
        }
