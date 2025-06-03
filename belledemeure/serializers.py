from rest_framework import serializers
from .models import Property, Amenity

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name']

class PropertySerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Property
        fields = [
            'id',
            'property_type',
            'owner',
            'title',
            'description',
            'address',
            'district',
            'rooms',
            'has_furniture',
            'has_appliances',
            'has_wifi',
            'has_parking',
            'transport',
            'price_per_night',
            'is_available',
            'created_at',
            'amenities',
        ]