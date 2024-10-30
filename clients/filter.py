import django_filters
from .models import Client
from django.db.models import Q

class ClientFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search')

    class Meta:
        model = Client
        fields = []

    def search_filter(self, queryset, name, value):
        # Filter by first_name, last_name, or company
        return queryset.filter(
            Q(first_name__icontains=value) | 
            Q(last_name__icontains=value) | 
            Q(address__icontains=value) |
            Q(region__icontains=value) | 
            Q(phone_home__icontains=value) 
        )
