class TestData:
    """
    class houses data that will be used for the 
    different test scenarios.
    """

    def __init__(self):
        self.signup_data = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanya1234"
        }
        self.blank_username_on_signup = {
            "first_name": "",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanya1234"
        }
        self.blank_email_on_signup = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "",
            "password": "@sanya1234"
        }
        self.blank_password_on_signup = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": ""
        }
        self.invalid_email_on_signup = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennethtgmail.com",
            "password": "@sanya1234"
        }
        self.invalid_password_on_signup = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "saewewewewewewewew"
        }
        self.invalid_password_length = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sa32"
        }
        self.login_data = {
            "email": "test@example.com",
            "password": "12345678@90S"
        }
        self.login_data2 = {
            "user": {
                "email": "kenned@gmail.com",
                "password": "kenned123456"
            }
        }
        self.login_data_admin = {
            "user": {
                "email": "admin@gmail.com",
                "password": "admin123456"
            }
        }
        self.wrong_login_data = {
            "email": "sanyakenneth@gmail.com",
            "password": "sanya1234"
            
        }
        self.blank_email = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": ""
        }
        self.no_email_on_login = {
            "password": "kensanya1234"
        }
        self.no_password_on_login = {
            "email": "sanyakenneth@gmail.com"
        }
        self.invalid_firstname = {
            "first_name": "sa",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanya1234"
        }
        self.invalid_password = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanya1"
        }
        self.non_numeric_password = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanyadsdsderr"
        }
        self.password_with_space = {
            "first_name": "sanyat",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sa ny a1234"
        }
        self.firstname_with_no_characters = {
            "first_name": ".......",
            "last_name": "kent",
            "phone_number": "0789324528",
            "email": "sanyakennetht@gmail.com",
            "password": "@sanya1234"
        }
