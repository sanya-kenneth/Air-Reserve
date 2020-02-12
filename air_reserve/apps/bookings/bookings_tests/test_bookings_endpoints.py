from django.urls import reverse
from .base import BaseTestCase
import json


class BookingsTestCase(BaseTestCase):
    """
    Class Test Case for Bookings
    """

    def test_api_can_book_flight(self):
        url = '/api/v1/flights/1/bookings'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["message"], "flight booked successfuly")

    def test_api_gets_bookings(self):
        url = reverse("list_bookings")
        url_b = '/api/v1/flights/1/bookings'
        self.client.post(url_b, HTTP_AUTHORIZATION=self.auth_header, format="json")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'][0]['flight'], 1)

    def test_api_gets_one_booking(self):
        url = '/api/v1/bookings/3'
        url_b = '/api/v1/flights/1/bookings'
        self.client.post(url_b, HTTP_AUTHORIZATION=self.auth_header, format="json")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.data['data']['flight']['destination'], 'Kampala')
        self.assertEqual(response.status_code, 200)

    def test_user_can_cancel_booking(self):
        url = '/api/v1/bookings/4/cancel'
        url_b = '/api/v1/flights/1/bookings'
        self.client.post(url_b, HTTP_AUTHORIZATION=self.auth_header, format="json")
        response = self.client.patch(url, HTTP_AUTHORIZATION=self.auth_header, format="json")
        self.assertEqual(response.data['message'], 'your flight booking was cancelled')
        self.assertEqual(response.status_code, 200)
