# search/views.py
from rest_framework.generics import ListAPIView
from belledemeure.models import Property
from belledemeure.serializers import PropertySerializer
from django.db.models import Q


class PropertySearchView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = super().get_queryset()


        keyword = self.request.query_params.get("q")
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) |
                Q(description__icontains=keyword)
            )


        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        location = self.request.query_params.get("location")
        if location:
            queryset = queryset.filter(location__icontains=location)

        rooms_min = self.request.query_params.get("rooms_min")
        rooms_max = self.request.query_params.get("rooms_max")
        if rooms_min:
            queryset = queryset.filter(rooms__gte=rooms_min)
        if rooms_max:
            queryset = queryset.filter(rooms__lte=rooms_max)

        housing_type = self.request.query_params.get("type")
        if housing_type:
            queryset = queryset.filter(housing_type__iexact=housing_type)

        ordering = self.request.query_params.get("ordering")
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset



