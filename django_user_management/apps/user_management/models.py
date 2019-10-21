from django.contrib.auth.models import AbstractUser
from django.db import models
from django_iban.fields import IBANField


class CustomUser(AbstractUser):
    iban = IBANField(enforce_database_constraint=True, unique=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,)
    REQUIRED_FIELDS = ['iban', 'first_name', 'last_name', 'email']
