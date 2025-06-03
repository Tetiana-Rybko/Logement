from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from belledemeure.models import Property
from belledemeure.serializers import PropertySerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import SearchQuery
from .serializers import SearchQuerySerializer


class PropertySearchView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'description']
    ordering_fields = ['price_per_night', 'created_at']

    filterset_fields = {
        'price_per_night': ['gte', 'lte'],
        'rooms': ['gte', 'lte'],
        'address': ['icontains'],
        'property_type': ['exact'],
    }

    def list(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None

        query_text = request.query_params.get("search") or request.query_params.get("q") or ""

        if user and query_text:
            SearchQuery.objects.create(user=user, query=query_text)

        return super().list(request, *args, **kwargs)



class SearchQueryHistoryView(ListAPIView):
    serializer_class = SearchQuerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SearchQuery.objects.filter(user=self.request.user).order_by('-timestamp')