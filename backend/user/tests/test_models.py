from django.test import TestCase, Client
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''
            Test that creating a user with an email is successful
        '''
        email = 'test@gmail.com'
        password = '456@3'
        username = 'test1'

        user = get_user_model().objects.create_user(
            email = email,
            username = username
        )
        user.set_password(password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalised(self):
        '''
            Test that user email used to sign in is normalized
        '''
        email = 'test@STONEWELLTECH.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())
    
    def test_create_user_invalid_email(self):
        '''
            Test creating user with no email raises an error
        '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
         '''Test creating a superuser'''
         user = get_user_model().objects.create_superuser(
             'test@stonewelltech.com',
             'test123'
         )

         self.assertTrue(user.is_superuser) # is_superuser is added by PermissionsMixin
         self.assertTrue(user.is_staff)

class UserModelTests(TestCase):
    '''
        Test whether the user characteristics are saved well
    '''
    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@stonewelltech.com',
            username = 'Test username'
        )
        user.set_password(password)