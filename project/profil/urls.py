from . import views
from django.urls import path


urlpatterns = [
    path('profi/',views.profi,name='profi'),
    path('fprofil/',views.fprofil,name='fprofil'),
     
]