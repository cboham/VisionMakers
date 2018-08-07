from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls, name = 'admin'),
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
    path('', include('users.urls')),
    path('patients/', include('patients.urls')),
]
