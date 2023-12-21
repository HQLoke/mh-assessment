from django.urls import path, include
from .views import OutletList

urlpatterns = [
    path('outlets/', OutletList.as_view(), name='outlet-list')
]
