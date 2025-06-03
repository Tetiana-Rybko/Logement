from rest_framework import serializers
from .models import Review,Property

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())
    property_detail = serializers.StringRelatedField(read_only=True, source='property')

    class Meta:
        model = Review
        fields = ['id', 'user', 'property','property_detail','rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'property', 'created_at']