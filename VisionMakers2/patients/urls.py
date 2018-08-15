from . import views
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
app_name = 'patients'
urlpatterns = [
    path('select-patient/', views.select_patient, name = 'select_patient'),
    path('view/<pk>/', login_required(views.PatientUpdate.as_view()) , name = 'view_patient'),
    path('vision-rx/<pk>/', views.vision_rx, name = 'vision_rx'),
    path('vision-rx/spectacle-rx/<int:pk>/', login_required(views.SpectacleRxDetail.as_view()), name = 'spectacle-update'),
    path('vision-rx/contact-lens-rx/<int:pk>/', login_required(views.ContactLensRxDetail.as_view()), name = 'contact-lens-update'),
    re_path(r'^vision-rx/spectacle-rx/create/(?P<patient_id>[0-9]+)/$', login_required(views.SpectacleRxCreate.as_view()), name = 'spectacle-create'),
    re_path(r'^vision-rx/contact-lens-rx/create/(?P<patient_id>[0-9]+)/$', login_required(views.ContactLensRxCreate.as_view()), name = 'contact-lens-create'),
    path('insurance-summary/<pk>/', views.insurance_summary, name = 'insurance-summary'),
    path('insurance/med-ins/update/<int:pk>', login_required(views.MedicalInsDetail.as_view()), name = 'med-ins-update'),
    path('insurance/vis-ins/update/<int:pk>', login_required(views.VisionInsDetail.as_view()), name = 'vis-ins-update'),
    path('vision-rx/send-email/<pk>/', views.email_rx, name = 'email-rx'),
]
