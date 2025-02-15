from django.urls import path
from .views import flight_search, hotel_search

urlpatterns = [
    path('flights/', flight_search, name='flight_search'),
    path('hotels/', hotel_search, name='hotel_search'),
]
