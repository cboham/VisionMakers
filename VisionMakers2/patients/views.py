from django.shortcuts import render
from .filters import PatientFilter
from .models import Patient
from django.views.generic.edit import UpdateView
from django.urls import reverse
def select_patient(request):
    filter = PatientFilter(request.GET, queryset=Patient.objects.all())
    return render(request, 'patients/select_patient.html', {'filter': filter})

# def view_patient(request, id):
#     patient = Patient.objects.all().get(pk = id)
#     return render(request, 'patients/view_patient.html', {'patient': patient})

def vision_rx(request, pk):
    patient = Patient.objects.all().get(pk = pk)
    ordered_rxs = patient.common_rx_set.all().order_by('exam_date')
    return render(request, 'patients/patient_visionrx.html', {'patient': patient})

class PatientUpdate(UpdateView):
    model = Patient
    fields = [
        'cos_ptid',
        'first',
        'middle',
        'last',
        'nickname',
        'gender',
        'address',
        'address2',
        'city',
        'state',
        'zip',
        'location',
        'email',
        'home_phone',
        'cell_phone',
        'work_phone',
        'birthdate',
        'student',
        'SSN',
        'notes',
        'alert',
        'outside_doc',
        'referred_to_doc',
    ]
    template_name_suffix = '_view_form'
    # success_url = reverse('patients:select_patient', kwargs={'pk': self.pk})

    # class Spectacle_Rx_Update(UpdateView):
    #     model = Spectacle_Rx
    #     fields = [
    #
    #     ]
