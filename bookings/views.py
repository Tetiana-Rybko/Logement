from rest_framework import generics, permissions, filters, serializers
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
import logging
from rest_framework.pagination import PageNumberPagination

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
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        property_obj = serializer.validated_data['property']

        if Booking.objects.filter(
            property=property_obj,
            end_date__gte=start_date,
            start_date__lte=end_date
        ).exists():
            logger.warning(f"User [{user}] tried to book an unavailable period for property [{property_obj}]")
            raise serializers.ValidationError("This property is already booked for the selected dates.")

        booking = serializer.save(user=user)
        logger.info(f"User [{user}] successfully created booking ID {booking.id}")


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

