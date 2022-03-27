from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, 
                                        PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_fields):
        '''
            Creates and saves new user using email
        '''
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email = self.normalize_email(email), **extra_fields)
        password = user.set_password(password)
        password = user.set_password(password)
        user.save(using = self._db)

        return (user)

    def create_superuser(self, email, password):
        ''' Creates a superuser '''
        
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return (user)

class User(AbstractBaseUser, PermissionsMixin):
    '''
        Custom user model that supports using email in stead of username
    '''

    email = models.EmailField(max_length = 256, unique = True)
    username = models.CharField(max_length = 256, unique = True, blank = True)
    first_name = models.CharField(max_length = 256, blank = True)
    last_name = models.CharField(max_length = 256, blank = True)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    joined_at = models.DateTimeField(blank = True)
    
    ACCOUNT_TYPE_CHOICES = [
        ('INDIV', 'individual'),
        ('CORP', 'corporate'),
    ]
    acount_type = models.CharField(max_length = 256, choices = ACCOUNT_TYPE_CHOICES, 
                                    default = 'CORP')

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()

    def __str__s(self):
        return (self.role_name)