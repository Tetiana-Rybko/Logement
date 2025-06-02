from .filters import PropertyFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,permissions,filters
from .models import Property
from .serializers import PropertySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



@api_view(['GET'])
def home(request):
    return Response({'message':'Wellcome to belledemeure '})

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]

    filterset_class = PropertyFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price_per_night', 'created_at', 'rooms']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('price_min', openapi.IN_QUERY, description="Minimum price per night",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('price_max', openapi.IN_QUERY, description="Maximum price per night",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('rooms_min', openapi.IN_QUERY, description="Minimum number of rooms",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('rooms_max', openapi.IN_QUERY, description="Maximum number of rooms",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('district', openapi.IN_QUERY, description="District (partial match)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('property_type', openapi.IN_QUERY, description="Property type (exact match)",
                              type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)