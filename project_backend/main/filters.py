from django_filters import rest_framework as filters
from main.models import *


class SectionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Section
        fields = ('name',)
