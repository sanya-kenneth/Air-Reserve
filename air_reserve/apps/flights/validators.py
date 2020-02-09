import datetime
from django.core.exceptions import ValidationError


def validate_field_type(field, *args: str):
    if args[0] == 'string':
        if not isinstance(field, str):
            raise ValidationError(f"{field} only allows strings")
    if args[0] == 'integer':
        if not isinstance(field, int):
            raise ValidationError(f"{field} only allows numbers")
    if args[0] == 'date_time':
        if not isinstance(field, datetime.date):
            raise ValidationError(f"{field} only allows a valid date")
    if args[0] == 'time':
        if not isinstance(field, datetime.time):
            raise ValidationError(f"{field} only allows a valid time")
