from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    OFFICE_CHOICES = (
        ('BV' , 'BV'),
        ('WD' , 'WD'),
        ('PA' , 'PA')
        )
    location = models.CharField(max_length = 5, choices = OFFICE_CHOICES)
    #additional information
    OCCUPATION_CHOICES = (
        ('DR', 'Doctor'),
        ('R', 'Receptionist'),
        ('O', 'Other')
    )
    occupation = models.CharField(max_length=5, choices = OCCUPATION_CHOICES)
