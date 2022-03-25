from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        After changing the requirement from username to email, we want to test
        the custom user model if we can create and log in successfuly
        username: test_user
        email: testuser@gmail.com
        password: Test123@

        Later, we would like to test the password strength but it has not been covered
        for now
        """

        username = "test_user"
        email = "testuser@gmail.com"
        password = "Test123@"

        user = get_user_model().objects.create_user(
            email = email,
            username = username,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
