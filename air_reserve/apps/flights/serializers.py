from rest_framework import serializers
from .models import Flights
from .validators import validate_field_type


class FlightsSerializer(serializers.ModelSerializer):
    """Serializer class for Flights """
    departing_from = serializers.CharField(
        validators=[validate_field_type('string')],
        required=True,
        error_messages={
            "required": "departing from field is required",
            "blank": "departing from field cannot be left blank"
        }
    )
    destination = serializers.CharField(
        validators=[validate_field_type('string')],
        required=True,
        error_messages={
            "required": "destination field is required",
            "blank": "destination field cannot be left blank"
        }
    )
    date_of_departure = serializers.DateField(
        validators=[validate_field_type('date')],
        required=True,
        error_messages={
            "required": "date of depature field is required",
            "blank": "date of depature field cannot be left blank"
        }
    )
    departure_time = serializers.TimeField(
        validators=[validate_field_type('time')],
        required=True,
        error_messages={
            "required": "depature time field is required",
            "blank": "depature time field cannot be left blank"
        }
    )
    fee = serializers.IntegerField(
        validators=[validate_field_type('integer')],
        required=True,
        error_messages={
            "required": "fee field is required",
            "blank": "fee field cannot be left blank"
        }
    )

    class Meta:
        model = Flights
        
        fields = ['departing_from', 'destination', 'date_of_departure',
                  'depature_time', 'fee']
