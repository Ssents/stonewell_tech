from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''
            Test that creating a user with an email is successful
        '''
        email = 'test@gmail.com'
        password = 'Test@35Ty%'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalised(self):
        '''
            Test that user email used to sign in is normalized
        '''
        email = 'test@STONEWELLTECH.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())