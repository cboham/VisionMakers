from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new-frame/add/', login_required(views.TypeCreate.as_view()), name = 'add-type'),
    path('existing-frame/add/', views.pair_create, name = 'add-pair'),
    path('frame-type/<int:pk>/', login_required(views.DetailView.as_view()), name = 'detail-type'),
    path('frame-type/<int:pk>/edit/', login_required(views.TypeUpdate.as_view()), name = 'edit-type'),
    path('frame-type/<int:pk>/delete/', login_required(views.TypeDelete.as_view()), name = 'delete-type'),
    path('frame-type/<int:pk>/print/', views.print_page, name = 'print-type'),
    path('search/', views.search, name = 'search'),
    path('search/multiupdate/<skus>', views.multiupdate, name = 'multiupdate'),
    path('submitted/', views.submission, name = 'submission'),
    path('export/xls/<location>/<title>', views.export_to_xls, name = 'export_to_xls'),
    path('export/', views.get_export, name = 'export'),

]
