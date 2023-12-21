from django.db import models

# Create your models here.
class Outlet(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=50, null=True)
    address = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ('name', 'state', 'address')
    
    def __str__(self):
        return f'Name: {self.name} Address: {self.address} (Lat: {self.latitude}, Long: {self.longitude})'