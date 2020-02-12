from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class BaseTestCase(APITestCase):
    """
    Class to setup tests for flights
    """

    fixtures = ['air_reserve/apps/authentication/fixtures/users.json',
                'air_reserve/apps/flights/fixtures/flights.json'
                ]

    login_data = {
        "email": "kenned@gmail.com",
        "password": "LuYun@123"
    }

    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('user_login')
        self.login_response = self.client.post(
            self.login_url, self.login_data, format='json')
        test_token = self.login_response.data['token']
        self.auth_header = 'Bearer {}'.format(test_token)
