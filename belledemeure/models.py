from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('rent', 'For Rent'),
    ]

    property_type = models.CharField(
        max_length=10,
        choices=PROPERTY_TYPE_CHOICES,
        default='rent'
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=50, blank=True, null=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)
    has_furniture = models.BooleanField(null=True, blank=True)
    has_appliances = models.BooleanField(null=True, blank=True)
    has_wifi = models.BooleanField(null=True, blank=True)
    has_parking = models.BooleanField(null=True, blank=True)
    transport = models.TextField(blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.title



