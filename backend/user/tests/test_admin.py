from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        '''
        The setup will create a user and log the user in before the concurrent tests are 
        done
        '''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@stonewelltech.com',
            password = 'pass.124@'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@stonewelltech.com',
            password = 'pass.234#',
            username = 'Test username'
        )
    
    def test_user_listed(self):
        ''' Test that users are listed on the admin user page '''
        url = reverse('admin:user_user_changelist')
        response = self.client.get(url)
        
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)
    
    def test_user_page_change(self):
        '''Test that user page edit works'''
        url = reverse('admin:user_user_change', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    