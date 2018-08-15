from django.db import models
from localflavor.us.models import USStateField, USZipCodeField, USSocialSecurityNumberField

class Insurance(models.Model):
    company_name = models.CharField(max_length = 30)
    type = models.CharField(
        max_length = 30,
        choices = (
            ('medical', 'medical'),
            ('vision', 'vision'),
            )
        )
    active = models.BooleanField()
    plan_name = models.CharField(max_length = 30)
    address1 = models.CharField(max_length = 40)
    address2 = models.CharField(max_length = 40, blank = True)
    city = models.CharField(max_length = 40)
    state = USStateField()
    zip = USZipCodeField()
    phone_number = models.CharField(max_length = 20)
    fax_number = models.CharField(max_length = 20, blank = True)
    contact_person = models.CharField(max_length = 40)
    notes = models.CharField(max_length = 250, blank = True)


    def __str__(self):
        return self.company_name + " - " + self.plan_name
