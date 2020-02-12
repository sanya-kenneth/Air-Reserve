from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .test_data import TestData


class BaseTestCase(APITestCase):
    """ 
    Base Test class for all tests in the app
    """

    def setUp(self):
        self.client = APIClient()
        self.data = TestData()
        User = get_user_model()
        self.user = User.objects.create_user(
            first_name='test', last_name='test1',email='test@example.com',
            phone_number='0743789121',password='12345678@90S'
        )
