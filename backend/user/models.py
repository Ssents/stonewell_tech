from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, 
    PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    '''
    Custom user manager to be used for CustomUser model
    '''

    def create_user(self, email, password=None, **extra_fields):
        '''
        Create and save new user
        '''

        user = self.model(email = email, **extrafields)
        user.set_password(password)
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom user model that has the following changes
    1. Supports using email other than username when signing is
    2. Checks whether user is staff of stonewell or a customer only
    '''

    email = models.EmailField(max_length = 256, unique = True)
    username = models.CharField(max_length = 100, unique = True)
    first_name = models.CharField(max_length = 256, blank = True)
    last_name = models.CharField(max_length = 256, blank = True)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'