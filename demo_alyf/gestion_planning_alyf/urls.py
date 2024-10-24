from django.urls import path
from . import views
from .views import CalendarView, CalendarDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('calendar/', CalendarView.as_view(), name='calendar'),
     path('moduledetails/<uuid:module_id>/', CalendarDetailView.as_view(), name='moduleinfo'),  
    #  path('login/', MyLoginView.as_view(), name='login_page'),
     path('home',views.home, name='home'),
     #path("personal", views.personalspace, name = "perso"),
     path("selectformateur/", views.selectformateur, name = "selectformateur"),
     path("telecharger/<str:file>/", views.telecharger_document, name= "telecharger_document"),
     path("logout/", LogoutView.as_view(), name = "logout")
     
    
     
     
    #  path('caltest/', views.test, name='test'),
    #  path('caltest2/', views.test2, name='test2')

    #  path('', views.affichercalendrier, name='affichercalendrier'),
   
    #  path('getmodule/', views.get_dicomodule, name='get_dicomodule')
]
