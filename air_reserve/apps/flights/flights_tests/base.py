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
        "email": "admin@gmail.com",
        "password": "LuYun@123"
    }
    data = {
        "departing_from": "Busia",
        "destination": "Kampala",
        "date_of_departure": "2020-7-27",
        "departure_time": "6:00",
        "fee": 2000
    }
    update_data = {
        "departing_from": "Bugiri",
        "destination": "Masaka",
        "date_of_departure": "2020-07-27",
        "departure_time": "6:00",
        "fee": 2000
    }

    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('user_login')
        self.login_response = self.client.post(
            self.login_url, self.login_data, format='json')
        test_token = self.login_response.data['token']
        self.auth_header = 'Bearer {}'.format(test_token)
        self.data = self.data
        self.update_data = self.update_data
