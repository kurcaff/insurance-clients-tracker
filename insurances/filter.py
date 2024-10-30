import django_filters
from .models import Insurance
from django.db.models import Q

class InsuranceFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search')

    class Meta:
        model = Insurance
        fields = []

    def search_filter(self, queryset, name, value):
        # Filter by first_name, last_name, or company
        return queryset.filter(
            Q(name__icontains=value) | 
            Q(street_name__icontains=value) | 
            Q(zip_code__icontains=value)
        )