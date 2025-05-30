from django.contrib import admin
from .models import Property, Amenity

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'address', 'price_per_night', 'is_available')
    list_filter = ('is_available', 'has_furniture', 'has_appliances')
    search_fields = ('title', 'description', 'address')

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
