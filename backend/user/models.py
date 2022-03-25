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
