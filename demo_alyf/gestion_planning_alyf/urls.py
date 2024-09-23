from django.urls import path
from . import views
from .views import CombinedCalendarView

urlpatterns = [
     path('calendar/', CombinedCalendarView.as_view(), name='combined_calendar'),
    #  path('caltest/', views.test, name='test'),
    #  path('caltest2/', views.test2, name='test2')

    #  path('', views.affichercalendrier, name='affichercalendrier'),
   
    #  path('getmodule/', views.get_dicomodule, name='get_dicomodule')
]