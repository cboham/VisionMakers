from django.shortcuts import render
from .filters import PatientFilter
from .models import Patient, Spectacle_Rx, Contact_Lens_Rx, Common_Rx
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.detail import DetailView
from django.core.mail import send_mail

@login_required
def select_patient(request):
    filter = PatientFilter(request.GET, queryset=Patient.objects.all())
    return render(request, 'patients/select_patient.html', {'filter': filter})

# def view_patient(request, id):
#     patient = Patient.objects.all().get(pk = id)
#     return render(request, 'patients/view_patient.html', {'patient': patient})
@login_required
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
    template_name_suffix = '_profile'

    # class Spectacle_Rx_Update(UpdateView):
    #     model = Spectacle_Rx
    #     fields = [
    #
    #     ]

class SpectacleRxDetail(UpdateView):
    template_name = 'patients/spectacle_rx_update.html'
    model = Spectacle_Rx
    fields = [
        'exam_date',
        'expires',
        'doctor',
        'notes',
        'od_sphere',
        'od_cylinder',
        'od_axis',
        'od_prism',
        'od_prism2',
        'od_add',
        'os_sphere',
        'os_cylinder',
        'os_axis',
        'os_prism',
        'os_prism2',
        'os_add',
        'sv_reading',
        'sv_distance',
    ]
    def get_context_data(self, **kwargs):
        context = super(SpectacleRxDetail, self).get_context_data(**kwargs)
        patient = self.object.patient
        context['patient'] = patient
        return context

class ContactLensRxDetail(UpdateView):
    template_name = 'patients/contact_lens_rx_update.html'
    model = Contact_Lens_Rx
    fields = [
        'exam_date',
        'expires',
        'doctor',
        'notes',
        'od_base_curve',
        'od_power',
        'od_power2',
        'od_ax',
        'od_diam',
        'od_add',
        'os_base_curve',
        'os_power',
        'os_power2',
        'os_ax',
        'os_diam',
        'os_add',
    ]
    def get_context_data(self, **kwargs):
        context = super(ContactLensRxDetail, self).get_context_data(**kwargs)
        patient = self.object.patient
        context['patient'] = patient
        return context

class SpectacleRxCreate(CreateView):
    template_name = 'patients/spectacle_rx_update.html'
    model = Spectacle_Rx
    fields = [
        'exam_date',
        'expires',
        'doctor',
        'notes',
        'od_sphere',
        'od_cylinder',
        'od_axis',
        'od_prism',
        'od_prism2',
        'od_add',
        'os_sphere',
        'os_cylinder',
        'os_axis',
        'os_prism',
        'os_prism2',
        'os_add',
        'sv_reading',
        'sv_distance',
    ]


    def get_context_data(self, **kwargs):
        context = super(SpectacleRxCreate, self).get_context_data(**kwargs)
        patient = Patient.objects.all().get(pk = self.kwargs['patient_id'])
        context['patient'] = patient
        return context

    def form_valid(self, form):
        form.instance.patient = Patient.objects.all().get(pk=self.kwargs['patient_id'])
        return super().form_valid(form)


class ContactLensRxCreate(CreateView):
    template_name = 'patients/contact_lens_rx_update.html'
    model = Contact_Lens_Rx
    fields = [
        'exam_date',
        'expires',
        'doctor',
        'notes',
        'od_base_curve',
        'od_power',
        'od_power2',
        'od_ax',
        'od_diam',
        'od_add',
        'os_base_curve',
        'os_power',
        'os_power2',
        'os_ax',
        'os_diam',
        'os_add',
    ]
    def get_context_data(self, **kwargs):
        context = super(ContactLensRxCreate, self).get_context_data(**kwargs)
        patient = Patient.objects.all().get(pk = self.kwargs['patient_id'])
        context['patient'] = patient
        return context

    def form_valid(self, form):
        form.instance.patient = Patient.objects.all().get(pk=self.kwargs['patient_id'])
        return super().form_valid(form)
    

    # def email_rx(request, common_id):
    #     rx = Common_Rx.objects.all().get(pk = common_id)
    #     if rx.os_sphere:
    #         type = 'Spectacle'
    #     else:
    #         type = 'Contact Lens'
    #     send_mail(
    #         subject = type + ' Rx',
    #         message =
    #         )
