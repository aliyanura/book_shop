from django_filters import rest_framework
from .models import Book


class BookFilter(rest_framework.FilterSet):
    price = rest_framework.RangeFilter()

    class Meta:
        model = Book
        fields = ['price', ]