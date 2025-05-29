from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # отображать имя пользователя
    property = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'property', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'property', 'created_at']