from . import views
from django.urls import path
app_name = 'users'
urlpatterns = [
    path('register/', views.create_profile, name = 'register'),
    path('index/', views.index, name = 'index'),
    path('', views.user_login, name = 'login'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),

]
