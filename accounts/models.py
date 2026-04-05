from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    '''
    Create_user validates that an email address is provided and creates a new user with the given email and password.
    Create_superuser creates a new superuser with the given email and password, ensuring that the is_staff and is_superuser flags are set to True.
    '''
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        extra_fields.setdefault('username', email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    '''CustomUser extends Django's AbstractUser and PermissionsMixin to create a custom user model that uses email as the unique identifier instead of username.
    It includes additional fields such as first_name, last_name, email, is_staff, is_active, date_joined, and organisation.
    '''

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    organisation = models.CharField(max_length=100, blank=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email