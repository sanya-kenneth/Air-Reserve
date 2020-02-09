import jwt
import datetime
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    """
    User Manager Class
    """

    def create_user(self, first_name, last_name, email,
                    phone_number=None, password=None):
        """
        Create and return a `User` with an email, firsname,
        lastname, phonenumber, and password.
        """
        user = self.model(first_name=first_name, last_name=last_name,
                          email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name,
                         email, password, phone_number=None):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this user is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('superusers must have a password.')
        user = self.create_user(first_name, last_name, email,
                                phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(db_index=True, max_length=255)
    last_name = models.CharField(db_index=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User Class Object`.
        This string is used when a `User` is printed in the console.
        """
        return self.email
    
    
    @staticmethod
    def encode_auth_token(email):
        """Generates auth token."""
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(
                    days=30),
                'iat': datetime.datetime.utcnow(),
                'sub': email
            }
            return jwt.encode(
                payload, settings.SECRET_KEY, algorithm='HS256'
            )
        except Exception as e:
            return e
