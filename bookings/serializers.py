from rest_framework import serializers
from bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        property = data.get('property')

        if start_date >= end_date:
            raise serializers.ValidationError('Start date must be before end date')

        overlapping = Booking.objects.filter(
            property=property,
            status='confirmed',
            start_date__lt=end_date,
            end_date__gt=start_date
        )
        if self.instance:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError('This property is already booked for the selected dates')

        return data