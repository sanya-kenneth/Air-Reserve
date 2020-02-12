from django.urls import reverse
from .base import BaseTestCase


class FlightTestCase(BaseTestCase):
    """
    Class Test Case for Flights
    """

    def test_api_creates_flight(self):
        url = '/api/v1/flights/'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self.auth_header, data=self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['data']['departing_from'], 'Busia')

    def test_returns_error_if_user_attempts_to_add_flight_twice(self):
        url = '/api/v1/flights/'
        self.client.post(url, HTTP_AUTHORIZATION=self.auth_header, data=self.data, format="json")
        response = self.client.post(url, HTTP_AUTHORIZATION=self.auth_header, data=self.data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.data['error']['error'][0], "flight already exists")

    def test_api_gets_flights(self):
        url = reverse("list_flights")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'][0]['departing_from'], 'Palisa')

    def test_api_gets_one_flight(self):
        url = '/api/v1/flights/1'
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.data['data']['destination'], 'Kampala')
        self.assertEqual(response.status_code, 200)

    def test_returns_error_if_flight_doesnot_exist(self):
        url = '/api/v1/flights/13'
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Not found.", str(response.data))

    def test_api_updates_flight_data(self):
        url = '/api/v1/flights/1/update'
        response = self.client.patch(url, HTTP_AUTHORIZATION=self.auth_header,
                                     data=self.update_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("flight data was updated", str(response.data))
