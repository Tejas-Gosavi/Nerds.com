import django_filters
from django.forms import Textarea

from comic.models import Comic


class ComicsFilter(django_filters.FilterSet):
    class Meta:
        model = Comic
        fields = {
            "title": ["icontains"],
            "brand": ["exact"],
            "comic_type": ["exact"],
            "price": ["lte", "gte"],
        }
