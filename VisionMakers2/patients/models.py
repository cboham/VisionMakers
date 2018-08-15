from django.db import models
from polymorphic.models import PolymorphicModel
from localflavor.us.models import USStateField, USZipCodeField, USSocialSecurityNumberField
from insurance.models import Insurance
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

    class Meta:
        verbose_name_plural = 'Common Rx\'s'

    def __str__(self):
        return self.doctor + ' - ' + self.exam_date

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

    class Meta:
        verbose_name_plural = 'Spectacle Rx\'s'

    def get_absolute_url(self):
        return reverse('patients:spectacle-update', kwargs={'pk': self.pk})

    def __str__(self):
        return super().__str__()

    def class_name(self):
        return 'spectacle'

    def dictionary(self):
        return {
            'od_sphere': self.od_sphere,
            'od_cylinder': self.od_cylinder,
            'od_axis': self.od_axis,
            'od_prism': self.od_prism,
            'od_prism2': self.od_prism2,
            'od_add':self.od_add,
            'os_sphere': self.os_sphere,
            'os_cylinder': self.os_cylinder,
            'os_axis': self.os_axis,
            'os_prism': self.os_prism,
            'os_prism2': self.os_prism2,
            'os_add':self.os_add,
        }

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

    def get_absolute_url(self):
        return reverse('patients:contact-lens-update', kwargs={'pk': self.pk})

    def __str__(self):
        return super().__str__()

    def class_name(self):
        return 'contact-lens'

    def dictionary(self):
        return {
            'od_base_curve': self.od_base_curve,
            'od_power':self.od_power,
            'od_power2':self.od_power2,
            'od_ax':self.od_ax,
            'od_diam':self.od_diam,
            'od_add':self.od_add,
            'os_base_curve':self.os_base_curve,
            'os_power':self.os_power,
            'os_power2':self.os_power2,
            'os_ax':self.os_ax,
            'os_diam':self.os_diam,
            'os_add':self.os_add,
        }

class Patient_Insurance(PolymorphicModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    member_id = models.IntegerField()
    plan_name = models.CharField(max_length = 30, blank = True)
    relation_to_insured = models.CharField(
            max_length = 20,
            choices = (
            ('self', 'Self'),
            ('spouse', 'Spouse'),
            ('child', 'Child'),
            ('other', 'Other')
        )
    )
    bill_payer = models.CharField(max_length = 30)
    bp_address1 = models.CharField(max_length = 40)
    bp_address2 = models.CharField(max_length = 40, blank = True)
    bp_city = models.CharField(max_length = 40)
    bp_state = USStateField()
    bp_zip = USZipCodeField()


    class Meta:
        verbose_name_plural = 'Patient Insurances'

    def __str__(self):
        return self.plan_name

class Vision_Ins(Patient_Insurance):
    vision_list = Insurance.objects.all().filter(type = 'vision').values_list('company_name')
    VISION_CHOICES = ()
    for i in range(len(vision_list)):
        VISION_CHOICES = VISION_CHOICES + ((vision_list[i][0], vision_list[i][0]),)
    company_name = models.CharField(max_length = 30, choices = VISION_CHOICES)

    class Meta:
        verbose_name_plural = 'Vision Insurances'

    def __str__(self):
        return self.company_name + ' - ' + super().__str__()

    def class_name(self):
        return 'vision'

    def get_absolute_url(self):
        return reverse('patients:vis-ins-update', kwargs={'pk': self.pk})

class Medical_Ins(Patient_Insurance):
    medical_list = Insurance.objects.all().filter(type = 'medical').values_list('company_name')
    MEDICAL_CHOICES = ()
    for i in range(len(medical_list)):
        MEDICAL_CHOICES = MEDICAL_CHOICES + ((medical_list[i][0], medical_list[i][0]),)
    company_name = models.CharField(max_length = 30, choices = MEDICAL_CHOICES)

    class Meta:
        verbose_name_plural = 'Medical Insurances'

    def class_name(self):
        return 'medical'

    def __str__(self):
        return self.company_name + ' - ' + super().__str__()

    def get_absolute_url(self):
        return reverse('patients:med-ins-update', kwargs={'pk': self.pk})
