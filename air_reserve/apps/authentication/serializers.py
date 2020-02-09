import re
from rest_framework import serializers
from validate_email import validate_email as \
    validate_user_email
from .models import User
from .validators import check_user_exists


class BaseSignupSerializer(serializers.ModelSerializer):
    """Base serializer class for creating new users"""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    # ensures that password is required and not blank
    first_name = serializers.CharField(
        max_length=120,
        min_length=3,
        trim_whitespace=True,
        required=True,
        error_messages={
            "required": "firstname field is required",
            "blank": "firstname field cannot be left blank",
        }
    )
    last_name = serializers.CharField(
        max_length=120,
        min_length=3,
        trim_whitespace=True,
        required=True,
        error_messages={
            "required": "lastname field is required",
            "blank": "lastname field cannot be left blank",
        }
    )
    email = serializers.EmailField(
        validators=[check_user_exists],
        required=True,
        error_messages={
            "required": "email field is required",
            "blank": "email field cannot be left blank",
        }
    )
    phone_number = serializers.CharField()
    password = serializers.CharField(
        max_length=18,
        min_length=8,
        write_only=True,
        required=True,
        error_messages={
            "required": "password field is required",
            "blank": "password field cannot be left blank",
        }
    )

    def validate_password(self, password):
        """
        validates that  password is longer than 8 characters
        password is alphanumeric
        """
        if not re.search(r'[0-9]', password) or not re.search(r'[a-zA-Z]', password) or not\
                re.search(r'[!?@#$%^&*.]', password):
            raise serializers.ValidationError(
                "password should include numbers and alphabets and one special character")
        if re.search(r'[\s]', password):
            raise serializers.ValidationError(
                "password should not include white spaces")
        return password

    def validate_name(name):
        """ validates names provided by the user"""
        if not re.search(r'[a-zA-Z]', name):
            raise serializers.ValidationError(
                "firstname or lastname should only contain characters")
        return name

    def validate_firstname(self, first_name):
        """Validates the user's first name """
        return validate_name(first_name)

    def validate_lastname(self, last_name):
        """Validates the user's last name """
        return validate_name(last_name)

    def validate_email(self, email):
        """ validates the user's email"""
        isvalid_email = validate_user_email(email)
        print(isvalid_email)
        email_exists = User.objects.filter(email=email)
        if not isvalid_email:
            raise serializers.ValidationError(
                "email provided is not valid"
            )
        if email_exists.exists():
            raise serializers.ValidationError(
                "email provided already exists")
        return email


class SignupUserSerializer(BaseSignupSerializer):
    """Serializer class for creating normal users """

    class Meta:
        model = User
        # List all of the fields that could possibly be
        # included in a request or response, including fields
        # specified explicitly above.
        fields = ['email', 'first_name', 'last_name', 'phone_number',
                  'password']

    def create(self, validated_data):
        # Use the `create_user` method to create a new user.
        return User.objects.create_user(**validated_data)


class SignupAdminSerializer(BaseSignupSerializer):
    """Serializer class for creating an admin/superuser """

    class Meta:
        model = User
        # List all of the fields that could possibly be
        # included in a request or response, including fields
        # specified explicitly above.
        fields = ['email', 'first_name', 'last_name', 'phone_number',
                  'password']

    def create(self, validated_data):
        # Use the `create_superuser` method to create a new admin/superuser.
        return User.objects.create_superuser(**validated_data)
