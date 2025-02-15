from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .amadeus_api import get_flights, get_hotels

@api_view(['GET'])
@renderer_classes([JSONRenderer])  # Ensures response is JSON, not HTML
def flight_search(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    budget = float(request.GET.get('budget', 0))

    flights = get_flights(origin, destination, budget)
    return Response(flights)

@api_view(['GET'])
@renderer_classes([JSONRenderer])  # Ensures response is JSON, not HTML
def hotel_search(request):
    city = request.GET.get('city')
    budget = float(request.GET.get('budget', 0))

    hotels = get_hotels(city, budget)
    return Response(hotels)
