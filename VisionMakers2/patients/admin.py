from django.contrib import admin
from .models import Patient, Patient_Insurance, Medical_Ins, Vision_Ins

admin.site.register(Patient)
admin.site.register(Medical_Ins)
admin.site.register(Vision_Ins)
