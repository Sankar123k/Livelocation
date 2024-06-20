from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lat: {self.latitude}, Long: {self.longitude} at {self.timestamp}"



