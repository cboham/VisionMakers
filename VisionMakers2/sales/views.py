from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SelectPatient, Glasses_Form


@login_required
def select_patient(request):
    if request.method == 'POST':
        form = SelectPatient(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient']

            if form.cleaned_data['purchase'] == 'glasses':
                return purchase_home(request, patient_id)
            else:
                return select_contacts(request, patient_id)
    else:
        form = SelectPatient()
    return render(request, 'sales/selection.html', {'form': form})

@login_required
def purchase_home(request, patient_id):
    context = {
        'patient':'Connor A Boham'
    }
    return render(request, 'sales/purchase_home.html', context)


@login_required
def select_glasses(request, patient_id):
    if request.method == 'POST':
        form = Glasses_Form(request.POST)
        if form.is_valid():
            return submission(
                request,
                heading = 'Confirm, then continue',
                heading2 = 'You selected this pair'
            )

def submission(request, **kwargs):
    tuple = ()
    for key, value in kwargs.items():
        tuple += ((key, value),)
    context = dict(tuple)
    return render(request, 'sales/submission.html', context)
