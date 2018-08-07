from . import views
from django.urls import path
app_name = 'patients'
urlpatterns = [
    path('select-patient/', views.select_patient, name = 'select_patient'),
    path('view/<pk>/', views.PatientUpdate.as_view() , name = 'view_patient'),
    path('<pk>/vision_rx/', views.vision_rx, name = 'vision_rx')
]
