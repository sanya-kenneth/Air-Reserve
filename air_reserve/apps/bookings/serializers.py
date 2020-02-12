from rest_framework import serializers
from .models import Bookings


class BookingsSerializer(serializers.ModelSerializer):
    """Serializer class to handle user bookings """
    
    class Meta:
        model = Bookings
        
        fields = ['user', 'flight', 'booking_cancelled',
                  'booked_at', 'updated_at', 'id']
