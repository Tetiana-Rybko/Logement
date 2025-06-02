import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')
    rooms_min = django_filters.NumberFilter(field_name='rooms', lookup_expr='gte')
    rooms_max = django_filters.NumberFilter(field_name='rooms', lookup_expr='lte')
    district = django_filters.CharFilter(field_name='district', lookup_expr='icontains')
    property_type = django_filters.CharFilter(field_name='property_type', lookup_expr='exact')

    class Meta:
        model = Property
        fields = ['price_min', 'price_max', 'rooms_min', 'rooms_max', 'district', 'property_type']