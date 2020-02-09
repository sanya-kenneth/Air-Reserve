from django.db import models
from air_reserve.apps.authentication.models import User
from air_reserve.apps.flights.models import Flights
from django.utils import timezone


class Bookings(models.Model):
    """Model class for craeting bookings in the system"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    booking_cancelled = models.BooleanField(default=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
