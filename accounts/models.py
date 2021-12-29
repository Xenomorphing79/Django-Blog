from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db import models
from django.contrib.auth.models import PermissionsMixin

class Profile(AbstractUser):
    username = CharField(max_length=30, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username