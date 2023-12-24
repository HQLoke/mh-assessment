from django.db.models import Q
from outlets.models import Outlet
import requests
from geopy.geocoders import Nominatim

# GEOCODE_API = 'https://geocode.maps.co/search?q='
GOOGLE_MAPS_API = 'https://maps.googleapis.com/maps/api/geocode/json'
API_KEY = 'AIzaSyDec4tPPifWEgibtqiSDU40zDjD0NxhPLg'

def get_geographical_coordinates():
    outlets_without_geodata = Outlet.objects.filter(
        Q(latitude__isnull=True), 
        Q(longitude__isnull=True))
    
    for outlet in outlets_without_geodata:
        params = {
            'address': outlet.address,
            'key': API_KEY,
        }
        print(f"Obtaining geographical data for {outlet.name}...")
        response = requests.get(GOOGLE_MAPS_API, params=params)
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            outlet.latitude = location['lat']
            outlet.longitude = location['lng']
            outlet.save()
        else:
            print("Location data not available for this address.")
