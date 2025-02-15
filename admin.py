from django.contrib import admin
from .models import Flight, Hotel

# Register your models here.
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("airline", "origin", "destination", "price", "currency", "departure_date")
    search_fields = ("airline", "origin", "destination")
    list_filter = ("departure_date", "airline")

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "price_per_night", "currency", "rating")
    search_fields = ("name", "location")
    list_filter = ("rating",)
