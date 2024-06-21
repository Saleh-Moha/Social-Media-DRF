from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):


    def create_user(self, email,username,first_name, last_name, date_of_birth, password=None, **extra_fields):

        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')


        return self.create_user(email, username, first_name, last_name, date_of_birth, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)



    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'username']


    def __str__(self):
        return self.username


class user_profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    profile_photo = models.ImageField(upload_to='src/usersprofilephotos', blank=True)
    is_private = models.BooleanField(default=False, blank=True, null=False)
    bio = models.TextField(max_length=400, blank=True)
    location = models.TextField(max_length=400, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)  # Make it optional for testing

    def __str__(self):
        return str(self.user)
