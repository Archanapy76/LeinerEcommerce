from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from datetime import timedelta
from ecom.manager import UserManager
import random
import string

class UserAuth(AbstractBaseUser,PermissionsMixin):
    
       
        email = models.EmailField(max_length=100, unique=True)
        fullname = models.CharField(max_length=100)
        otp = models.CharField(max_length=6, blank=True, null=True)
        otp_expiry = models.DateTimeField(blank=True, null=True)
        is_verified = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=timezone.now)
        objects = UserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['fullname']

        class Meta:
        
            verbose_name_plural = 'Users'

        
        def __str__(self):
            return self.email

        def genrate_otp(self):
            otp = ''.join(random.choices(string.digits, k=6))
            self.otp = otp
            self.otp_expiry = timezone.now() + timedelta(minutes=5)
            self.save()  
            return otp  

