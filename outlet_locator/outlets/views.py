from rest_framework import generics
from django.shortcuts import render
from .models import Outlet
from .serializer import OutletSerializer

# Create your views here.
class OutletList(generics.ListAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer