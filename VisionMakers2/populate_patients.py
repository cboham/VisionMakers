import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VisionMakers2.settings')

import django
django.setup()
import random
from patients.models import Patient
from faker import Faker

fakegen = Faker()

def populate(N = 20):

    for entry in range(N):
        fake_title = fakegen.prefix()
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_middle = fakegen.first_name()[0]
        fake_nickname = fakegen.first_name()
        fake_cos_ptid = fakegen.ean(length = 8)
        OFFICE_CHOICES = ['BV', 'PA', 'WD']
        fake_location = random.choice(OFFICE_CHOICES)
        fake_address = fakegen.address()
        fake_address2 = fakegen.address()
        fake_city = fakegen.city()
        fake_state = fakegen.state()
        fake_zip = fakegen.zipcode()
        fake_home_phone = fakegen.phone_number()
        fake_cell_phone = fakegen.phone_number()
        fake_work_phone = fakegen.phone_number()
        fake_email = fakegen.email()
        fake_birthdate = fakegen.date_of_birth()
        fake_ssn = fakegen.ssn()
        GENDER_CHOICES = ['M', 'F', 'O']
        fake_gender = random.choice(GENDER_CHOICES)
        fake_student = random.choice(['True', 'False'])
        fake_outside_doc = fakegen.name()
        fake_referred_doc = fakegen.name()

        patient = Patient.objects.get_or_create(
            first = fake_first,
            last = fake_last,
            middle = fake_middle,
            title = fake_title,
            nickname = fake_nickname,
            cos_ptid = fake_cos_ptid,
            location = fake_location,
            address = fake_address,
            address2 = fake_address2,
            city = fake_city,
            zip = fake_zip,
            state = fake_state,
            gender = fake_gender,
            home_phone = fake_home_phone,
            cell_phone = fake_cell_phone,
            work_phone = fake_work_phone,
            email = fake_email,
            SSN = fake_ssn,
            birthdate = fake_birthdate,
            student = fake_student,
            notes = 'nothing here',
            alert = 'no alerts',
            outside_doc = fake_outside_doc,
            referred_to_doc = fake_referred_doc
            )[0]




        patient.save()

if __name__ == '__main__':
    print('populating script!')
    populate(40)
    print('populating complete!')
