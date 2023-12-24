from rest_framework import generics
from django.shortcuts import render
from .models import Outlet
from .serializer import OutletSerializer
from django.contrib.gis.geos import Point

# Create your views here.
class OutletList(generics.ListAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    
def map_view(request):
    outlets = Outlet.objects.all()
    features = []
    
    for outlet in outlets:
        point = Point(outlet.longitude, outlet.latitude)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point.x, point.y],
            },
            "properties": {
                "name": outlet.name,
                "state": outlet.state,
                "address": outlet.address,
            },
        }
        features.append(feature)
        
    geojson_data = {
        "type": "FeatureCollection",
        "features": features,
    }
    
    return render(request, 'map.html', {'geojson_data': geojson_data})