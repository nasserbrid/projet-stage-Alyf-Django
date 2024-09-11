from django.urls import path
from . import views

urlpatterns = [
    path('', views.affichercalendrier, name='affichercalendrier'),
    path('getmodule/', views.get_dicomodule, name='getdicomodule')
]