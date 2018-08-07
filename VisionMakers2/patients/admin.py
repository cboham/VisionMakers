from django.contrib import admin
from .models import Patient, Common_Rx, Spectacle_Rx, Contact_Lens_Rx

admin.site.register(Patient)
admin.site.register(Common_Rx)
admin.site.register(Spectacle_Rx)
admin.site.register(Contact_Lens_Rx)
