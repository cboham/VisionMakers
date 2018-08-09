from . import views
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
app_name = 'patients'
urlpatterns = [
    path('select-patient/', views.select_patient, name = 'select_patient'),
    path('view/<pk>/', login_required(views.PatientUpdate.as_view()) , name = 'view_patient'),
    path('<pk>/vision_rx/', views.vision_rx, name = 'vision_rx'),
    path('vision_rx/spectacle_rx/<int:pk>/', login_required(views.SpectacleRxDetail.as_view()), name = 'spectacle-update'),
    path('vision_rx/contact_lens_rx/<int:pk>/', login_required(views.ContactLensRxDetail.as_view()), name = 'contact-lens-update'),
    re_path(r'^vision_rx/spectacle_rx/create/(?P<patient_id>[0-9]+)/$', login_required(views.SpectacleRxCreate.as_view()), name = 'spectacle-create'),
    re_path(r'^vision_rx/contact_lens_rx/create/(?P<patient_id>[0-9]+)/$', login_required(views.ContactLensRxCreate.as_view()), name = 'contact-lens-create'),


]
