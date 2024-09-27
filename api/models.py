"""
Candidate Model
"""

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Candidate(models.Model):
    """
    Candidate class
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

