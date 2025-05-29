from rest_framework import generics, permissions, filters, serializers
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
import logging
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



logger = logging.getLogger(__name__)

class BookingPagination(PageNumberPagination):
    page_size = 5

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = BookingPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'property__title', 'start_date']
    search_fields = ['property__title']
    ordering_fields = ['start_date', 'end_date', 'created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            logger.debug(f"Staff user [{user}] requested all bookings")
            return Booking.objects.all()
        logger.debug(f"Regular user [{user}] requested own bookings")
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        booking = serializer.save(user=user)
        logger.info(f"User [{user}] successfully created booking ID {booking.id}")

    @swagger_auto_schema(
        operation_description="Get list of bookings. Staff sees all, regular user sees only own.",
        manual_parameters=[
            openapi.Parameter('status', openapi.IN_QUERY, description="Filter by status", type=openapi.TYPE_STRING),
            openapi.Parameter('property__title', openapi.IN_QUERY, description="Filter by property title",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Filter by start date",
                              type=openapi.TYPE_STRING, format='date'),
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by property title",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Ordering by", type=openapi.TYPE_STRING),
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
        ],
        responses={200: BookingSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="\nCreate a new booking (with date validation)",
        request_body=BookingSerializer,
        responses={201: BookingSerializer, 400: "Bad Request"}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            logger.debug(f"Staff user [{user}] requested booking details")
            return Booking.objects.all()
        logger.debug(f"Regular user [{user}] requested own booking details")
        return Booking.objects.filter(user=user)

    @swagger_auto_schema(
        operation_description="Retrieve a single booking. Staff sees all, user sees only own.",
        responses={200: BookingSerializer, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a booking.",
        request_body=BookingSerializer,
        responses={200: BookingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update a booking.",
        request_body=BookingSerializer,
        responses={200: BookingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a booking.",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

