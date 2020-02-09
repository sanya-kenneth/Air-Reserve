from django.core.exceptions import ValidationError
from .models import User


def check_user_exists(email: str):
    """
    Function checks if user exists
    
    args: 
        email: email of user attempting to signup
    
    returns:
        Error if a user with the email given already exists
    """
    user = User.objects.filter(email=email)
    if user.exists():
        raise ValidationError(f"user with email {email} already exists")
