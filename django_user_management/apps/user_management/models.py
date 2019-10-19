from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
