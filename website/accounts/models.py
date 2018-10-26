from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('You must provide an email for user')
        if not password:
            raise ValueError('You must provide a password for user')

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)  # hash user password
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self.db)
        return user_obj

    def create_superuser(self, email, password):
        user_obj = self.create_user(email=email, password=password, is_staff=True, is_superuser=True)
        user_obj.save()
        return user_obj


class User(PermissionsMixin, AbstractBaseUser):
    email = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
