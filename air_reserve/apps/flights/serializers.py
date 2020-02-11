from rest_framework import serializers
from .models import Flights


class FlightsSerializer(serializers.ModelSerializer):
    """Serializer class for Flights """
    departing_from = serializers.CharField(
        required=True,
        error_messages={
            "required": "departing from field is required",
            "blank": "departing from field cannot be left blank"
        }
    )
    destination = serializers.CharField(
        required=True,
        error_messages={
            "required": "destination field is required",
            "blank": "destination field cannot be left blank"
        }
    )
    date_of_departure = serializers.DateField(
        required=True,
        error_messages={
            "required": "date of departure field is required",
            "blank": "date of departure field cannot be left blank"
        }
    )
    departure_time = serializers.TimeField(
        required=True,
        error_messages={
            "required": "departure time field is required",
            "blank": "departure time field cannot be left blank"
        }
    )
    fee = serializers.IntegerField(
        required=True,
        error_messages={
            "required": "fee field is required",
            "blank": "fee field cannot be left blank"
        }
    )
    
    def validate(self, data):
        """
        Function checks if a flight exists
        
        args: 
            data: data containing information for flight to create 
        
        returns:
            Error if a flight given already exists
        """
        data = dict(data)
        flight = Flights.objects.filter(departing_from=data['departing_from'],
                                        destination=data['destination'],
                                        date_of_departure=data['date_of_departure'],
                                        departure_time=data['departure_time'])
        if flight.exists():
            raise serializers.ValidationError(f"flight already exists")
        return data

    class Meta:
        model = Flights

        fields = ['departure_time', 'departing_from', 'destination', 'date_of_departure',
                   'fee', 'id']
