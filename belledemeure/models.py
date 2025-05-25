from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    amenities = models.ManyToManyField(Amenity, blank=True)
    PROPERTY_TYPE_CHOICES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]

    property_type = models.CharField(
        max_length=10,
        choices=PROPERTY_TYPE_CHOICES
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    has_furniture = models.BooleanField(null=True, blank=True)
    has_appliances = models.BooleanField(null=True, blank=True)
    has_wifi = models.BooleanField(null=True, blank=True)
    has_parking = models.BooleanField(null=True, blank=True)
    transport = models.TextField(blank=True, null=True)
    square_meters = models.PositiveIntegerField(null=True, blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    nearby_places = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    has_installment = models.BooleanField(null=True, blank=True)
    has_mortgage = models.BooleanField(null=True, blank=True)
    district = models.CharField(max_length=50,blank=True, null=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# Create your models here.
