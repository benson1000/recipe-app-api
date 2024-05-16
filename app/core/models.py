from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

# Create your models here.

class CustomUserManager(BaseUserManager):
    """ Manage for users """
    def create_user(self, email, password=None, **extra_fields):
        """create, save and return a new user"""
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user
 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """User i the system"""
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
