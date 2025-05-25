from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__username', 'property__title')

# Register your models here.
