from amadeus import Client, ResponseError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API credentials
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")

if not AMADEUS_API_KEY or not AMADEUS_SECRET:
    raise ValueError("Amadeus API credentials are missing! Check your .env file.")

# Initialize Amadeus Client
amadeus = Client(client_id=AMADEUS_API_KEY, client_secret=AMADEUS_SECRET)

def get_flights(origin, destination, budget_per_traveler):
    """ Fetch flights within the budget per traveler """
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            maxPrice=int(budget_per_traveler),
            currencyCode='USD'
        )
        return response.data
    except ResponseError as error:
        return {"error": str(error)}

def get_hotels(city, budget_per_traveler):
    """ Fetch hotels within the budget per traveler """
    try:
        response = amadeus.shopping.hotel_offers_search.get(
            cityCode=city,
            currency='USD',
            priceRange=f'1-{int(budget_per_traveler)}'
        )
        return response.data
    except ResponseError as error:
        return {"error": str(error)}
