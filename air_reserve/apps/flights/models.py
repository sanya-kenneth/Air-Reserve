from django.db import models


class Flights(models.Model):
    """Model class for creating flights"""
    departing_from = models.CharField(db_index=True, max_length=120)
    destination =  models.CharField(db_index=True, max_length=120)
    date_of_departure = models.DateField()
    departure_time = models.TimeField()
    fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """return string representation of this class"""
    return f'flight from {departing_from} to {destination}'
