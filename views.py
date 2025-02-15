from rest_framework.response import Response
from rest_framework.decorators import api_view
from .amadeus_api import get_flights, get_hotels  # Ensure these are properly imported

@api_view(['GET'])
def flight_search(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    total_budget = request.GET.get('budget', 0)
    travelers = request.GET.get('travelers', 1)  # Default to 1 traveler

    try:
        total_budget = float(total_budget)
        travelers = int(travelers)

        if travelers <= 0:
            return Response({"error": "Number of travelers must be at least 1"}, status=400)

        if total_budget <= 0:
            return Response({"error": "Budget must be greater than 0"}, status=400)

        # Divide total budget among travelers
        budget_per_traveler = total_budget / travelers

        flights = get_flights(origin, destination, budget_per_traveler)
        return Response(flights)

    except ValueError:
        return Response({"error": "Invalid input for budget or travelers"}, status=400)


@api_view(['GET'])
def hotel_search(request):
    city = request.GET.get('city')
    total_budget = request.GET.get('budget', 0)
    travelers = request.GET.get('travelers', 1)  # Default to 1 traveler

    try:
        total_budget = float(total_budget)
        travelers = int(travelers)

        if travelers <= 0:
            return Response({"error": "Number of travelers must be at least 1"}, status=400)

        if total_budget <= 0:
            return Response({"error": "Budget must be greater than 0"}, status=400)

        # Divide total budget among travelers
        budget_per_traveler = total_budget / travelers

        hotels = get_hotels(city, budget_per_traveler)
        return Response(hotels)

    except ValueError:
        return Response({"error": "Invalid input for budget or travelers"}, status=400)
