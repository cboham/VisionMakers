from django.db import models
from polymorphic.models import PolymorphicModel
from localflavor.us.models import USStateField, USZipCodeField, USSocialSecurityNumberField
from datetime import date
from django.urls import reverse
class Patient(models.Model):

    '''Name and title'''
    TITLE_CHOICES = (
        ('', '-----'),
        ('Mr.' , 'Mr.'),
        ('Mrs.' , 'Mrs.'),
        ('Ms.' , 'Ms.'),
        ('Dr.', 'Dr.')
    )
    title = models.CharField(max_length = 5, choices =TITLE_CHOICES)
    first = models.CharField(max_length = 40)
    middle = models.CharField(max_length = 1, blank = True)
    last = models.CharField(max_length = 40)
    nickname = models.CharField(max_length = 20, blank = True)
    cos_ptid = models.IntegerField()

    '''Location and address'''
    OFFICE_CHOICES = (
        ('BV' , 'BV'),
        ('WD' , 'WD'),
        ('PA' , 'PA')
    )
    location = models.CharField(max_length = 5, choices = OFFICE_CHOICES)
    address = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 40)
    state = USStateField()
    zip = USZipCodeField()

    '''Communication'''
    home_phone = models.CharField(max_length = 25, blank = True)
    work_phone = models.CharField(max_length = 25,  blank = True)
    cell_phone = models.CharField(max_length = 25,  blank = True)

    email = models.EmailField()
    birthdate = models.DateField()
    SSN = USSocialSecurityNumberField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length = 5, choices = GENDER_CHOICES)
    student = models.BooleanField()
    notes = models.CharField(max_length = 500, blank = True)
    alert = models.CharField(max_length = 100, blank = True)
    outside_doc = models.CharField(max_length = 50)
    referred_to_doc = models.CharField(max_length = 50)


    def get_absolute_url(self):
        return reverse('patients:view_patient', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last

    @property
    def age(self):
        '''calculate the age of the person'''
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

class Common_Rx(PolymorphicModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    exam_date = models.DateField()
    expires = models.DateField()
    doctor = models.CharField(max_length = 30)
    notes = models.CharField(max_length = 256)


class Spectacle_Rx(Common_Rx):
    od_sphere = models.IntegerField()
    od_cylinder = models.IntegerField()
    od_axis = models.IntegerField()
    od_prism = models.IntegerField()
    od_prism2 = models.IntegerField()
    od_add = models.IntegerField()

    os_sphere = models.IntegerField()
    os_cylinder = models.IntegerField()
    os_axis = models.IntegerField()
    os_prism = models.IntegerField()
    os_prism2 = models.IntegerField()
    os_add = models.IntegerField()

    sv_reading = models.BooleanField()
    sv_distance = models.BooleanField()

class Contact_Lens_Rx(Common_Rx):
    od_base_curve = models.IntegerField()
    od_power = models.IntegerField()
    od_power2 = models.IntegerField()
    od_ax = models.IntegerField()
    od_diam = models.IntegerField()
    od_add = models.IntegerField()

    os_base_curve = models.IntegerField()
    os_power = models.IntegerField()
    os_power2 = models.IntegerField()
    os_ax = models.IntegerField()
    os_diam = models.IntegerField()
    os_add = models.IntegerField()
