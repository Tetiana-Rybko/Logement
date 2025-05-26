from rest_framework import generics, permissions,filters
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'property__title', 'start_date']
    search_fields = ['property__title']
    ordering_fields = ['start_date', 'end_date', 'created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            logger.debug(f"User staff [{user}]:requestet all bookings")
            return Booking.objects.all()
        logger.debug(f"User staff [{user}]:requestet your bookings")
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        booking = serializer.save(user=user)
        logger.info(f"User staff [{user}] created booking ID {booking.id}")



class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            logger.debug(f"[{user}]staff user:requestet all bookings")
            return Booking.objects.all()
        logger.debug(f"[{user}]requestet your bookings")
        return Booking.objects.filter(user=user)


