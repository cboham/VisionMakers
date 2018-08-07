from django import forms
from patients.models import Patient
from inventory.models import Type, Pair


class SelectPatient(forms.Form):
    patient_list = Patient.objects.all().distinct()
    PATIENT_CHOICES = (('X', '-------------------------'),)
    for i in range(len(patient_list)):
        PATIENT_CHOICES = PATIENT_CHOICES + ((patient_list[i].id, patient_list[i]),)

    patient = forms.ChoiceField(choices = PATIENT_CHOICES)
    PURCHASE_CHOICES = (
        ('glasses', 'Glasses'),
        ('contacts', 'Contacts'),
    )
    purchase = forms.ChoiceField(choices = PURCHASE_CHOICES)
    def clean_patient(self):
        file_name = self.cleaned_data['patient']
        if file_name == 'X':
            raise forms.ValidationError('Pick a patient')
        return file_name
    # # patient.widget.attrs.update({'class': 'page1'})
    #
    # type_list = Type.objects.order_by().values_list('sku').distinct()

    # # type.widget.attrs.update({'class': 'page2'})
    #
class Glasses_Form():
    type_list = Type.objects.all()
    TYPE_CHOICES = ()
    for i in range(len(type_list)):
        TYPE_CHOICES = TYPE_CHOICES + ((type_list[i], type_list[i]),)
    type = forms.ChoiceField(choices = TYPE_CHOICES)
    pair_list = Pair.objects.all()
    PAIR_CHOICES = ()
    for i in range(len(pair_list)):
        PAIR_CHOICES = PAIR_CHOICES + ((pair_list[i], pair_list[i]),)
        type = forms.ChoiceField(choices = TYPE_CHOICES)
    
