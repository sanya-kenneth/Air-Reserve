from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from air_reserve.apps.authentication.models import User
from .base import BaseTestCase


class UserSignUpAndLoginTestCase(BaseTestCase):
    """
    Class Test Case for testing user signup 
    functionality
    """

    def test_can_sign_up_user(self):
        """
        Method tests if the user can successfuly signup 
        """
        url = reverse('user_signup')
        response = self.client.post(url, self.data.signup_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['first_name'], 'sanyat')

    def test_returns_error_if_first_name_is_blank_on_signup(self):
        url = reverse('user_signup')
        response = self.client.post(
            url, self.data.blank_username_on_signup, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("firstname field cannot be left blank",
                      response.data['error']['first_name'][0])
    
    def test_returns_error_if_useremail_is_blank_on_signup(self):
        url = reverse('user_signup')
        response = self.client.post(
            url, self.data.blank_email_on_signup, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email field cannot be left blank",
                      response.data['error']['email'][0])
    
    def test_returns_error_if_password_is_blank_on_signup(self):
        url = reverse('user_signup')
        response = self.client.post(
            url, self.data.blank_password_on_signup, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password field cannot be left blank",
                      response.data['error']['password'][0])

    def test_returns_error_if_password_is_short(self):
        url = reverse('user_signup')
        response = self.client.post(
            url, self.data.invalid_password_length, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password should atleast be 8 characters.",
                      response.data['error']['password'][0])

    def test_returns_error_if_email_is_invalid(self):
        url = reverse('user_signup')
        response = self.client.post(
            url, self.data.invalid_email_on_signup, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Enter a valid email address",
                      response.data['error']['email'][0])

    def test_register_invalid_firstname(self):
        """test fail when firstname is invalid"""
        url = reverse('user_signup')
        response = self.client.post(url, self.data.invalid_firstname, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['first_name'][0], 'firstname should be atleast 3 characters long')

    def test_register_invalid_password(self):
        """test fail when password is invalid"""
        url = reverse('user_signup')
        response = self.client.post(url, self.data.invalid_password, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['password']
                         [0], 'password should atleast be 8 characters.')

    def test_register_non_alphanumeric_password(self):
        """test fail when password is not alphanumeric"""
        url = reverse('user_signup')
        response = self.client.post(url, self.data.non_numeric_password, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['password'][0],
                         'password should include numbers and alphabets and one special character')

    def test_register_password_with_whitespace(self):
        """test fail when password has spaces"""
        url = reverse('user_signup')
        response = self.client.post(url, self.data.password_with_space, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['password'][0],
                         'password should not include white spaces')
    
    def test_user_exists(self):
        """Test register with email that exists """
        url = reverse('user_signup')
        response = self.client.post(url, self.data.signup_data, format="json")
        response = self.client.post(url, self.data.signup_data ,format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_login(self):
        """
        Method tests the user login functionality
        """
        url = reverse('user_login')
        response = self.client.post(url, self.data.login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['token'])
        self.assertIsInstance(response.data['token'], str)
        self.assertEqual(response.data['message'], 'login was successful')

    def test_returns_error_if_user_credentials_are_wrong_on_login(self):
        """
        Method tests if the API returns an error
        if a user provides wrong credentials on login
        """
        url = reverse('user_login')
        response = self.client.post(
            url, self.data.wrong_login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("user email or password is incorrect",
                      response.data['error']['error'][0])