# from django.views import View
# from django.shortcuts import render
# from django.http import HttpResponse
# from .services.ExcelFile import ExcelFile
# from .services.Module import Module
# from .services.CalendrierPlanning import Calendar
# from datetime import time, date, datetime, timedelta
# import time 
# import win32com.client
# import pandas as pd
# from dotenv import load_dotenv
# import calendar
# from django.utils.safestring import mark_safe
# import pythoncom


# load_dotenv() 


# #test de la fonction context_data

# class CalendarView(View):
    
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         return render(request, 'myapp/calendar.html', context)

#     def get_context_data(self, **kwargs):
#         context = {}
#         d = self.get_date(self.request.GET.get('month', None))
#         cal = calendar.Calendar()
#         html_cal = cal.formatmonth(d.year, d.month)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = self.prev_month(d)
#         context['next_month'] = self.next_month(d)
#         return context

#     def get_date(self, req_month):
#         if req_month:
#             year, month = (int(x) for x in req_month.split('-'))
#             return date(year, month, 1)
#         return datetime.today()

#     def prev_month(self, d):
#         first = d.replace(day=1)
#         prev_month = first - timedelta(days=1)
#         month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#         return month

#     def next_month(self, d):
#         days_in_month = calendar.monthrange(d.year, d.month)[1]
#         last = d.replace(day=days_in_month)
#         next_month = last + timedelta(days=1)
#         month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#         return month    
    


# def affichercalendrier(request):
#     # Exemple simple de lecture et d'affichage du planning
#     pythoncom.CoInitialize()
    
#     calendrier_test = Calendar(2024)
#     test_excel_file = ExcelFile() 
    
#     test_excel_file.open_worksheet("DEV WEB")
#     test_excel_file.get_formateur_worksheet("HUYNH")
#     data = test_excel_file.create_modules()
    

#     # calendrier_test.add_event(11,2,{"id_module": 5, "nom_module": "Nasser et Igor"})
#     # calendrier_test.add_event(11,2,{"id_module": 6, "nom_module": "Black Clover"})
#     calendrier_test.dictionaries_module_to_calendar(data)
   

#     # calendrier_test.get_events_for_day(12,8)
#     # calendrier_test.formatday(12,8)
    
#     # calendrier_test.formatweek(3,12)
    
#     event = calendrier_test.formatmonth(11)
    
#     # event = calendrier_test.create_html_cal()

    
#     return render(request, 'calendar.html', {'event': event})



# def get_dicomodule(request):
#     pythoncom.CoInitialize()
    
    
#     test_excel_file = ExcelFile() 
    
  
#     test_excel_file.open_worksheet("DEV WEB")
#     test_excel_file.get_formateur_worksheet("HUYNH")
#     data = test_excel_file.create_modules()
#     # data = {"excel": test_excel_file}
#     return render(request, "calendar.html", {'data':data})
   
import email

from django.urls import reverse_lazy
from .services.Module import Module
import json
from django.views import View
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .services.ExcelFile import ExcelFile
from .services.Formateur import Formateur
from .services.CalendrierPlanning import Calendar  # Ton calendrier personnalisé
from datetime import date, datetime, timedelta
import calendar
import pythoncom
from django.core.cache import cache
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.auth.views import LoginView
from .models import *
from django.contrib.messages import get_messages
import sys
import logging
logger = logging.getLogger(__name__)

# class MyLoginView(LoginView):

 



#     def form_valid(self,  form):
     
#         logger.debug("Form is valid!")
       
#         return super().form_valid(form)

#     def form_invalid(self, form):
        
#         logger.debug("Form is invalid!")
      
#         messages.error(self.request, "wrong password")
#         return super().form_invalid(form)

    # Utilisez le nom de votre template de connexion existant
    #success_url = reverse_lazy('home')  # Remplacez 'home' par le nom de votre page d'accueil

    # def get(self, request, *args, **kwargs):
    #     print("Hello Nasser and Igor, Yoroshiku Onegaishimasu")
    #     return super().get(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
        
       
    #     print("Post in action!")
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     print(f"{username} username")
        

        # if not User.objects.filter(username=username).exists():
        #     messages.error(request, 'Invalid Email')
          
        #     print("email not found ")
        #     return redirect('login')

        # user = authenticate(request, username=username, password=password)
        # print(user)
        # if user is None:
        #     print("Authentication failed, user is None")
        #     sys.stdout.flush()
        #     messages.error(request, "Invalid Password")
        #     return self.form_invalid(self.get_form()) 
        
        # else:
        #         print("in the else")
        #     # Log in the user and redirect to the home page upon successful login
        #         login(request, user)
        #         return redirect('/home/')
        # return super().post(request, *args, **kwargs)



def home(request):
     
     if request.user.is_authenticated:
        
        return redirect("selectformateur/")




     

     

     
     

  
     return render(request, 'home.html')


def selectformateur(request):
     
    
        
    return render(request, "selectformateur.html")

        
    

class CalendarView(View):
    
   
    
    
    """_summary_
    """
    def get(self, request , *args, **kwargs):
       
        context = self.get_context_data()
        return render(request, 'calendar.html', context)
    
    
    def post(self, request, *args, **kwargs):
        selected_instructor = request.POST.get('instructorname')  # Get the selected value from the form
        context = self.get_context_data(instructor=selected_instructor)
        return render(request, 'calendar.html', context)

    """_summary_
    """
    def get_context_data(self, instructor=None, file=None ,**kwargs):
        print(f"{self.request.GET.get} post object ")
        context = {}
        d = self.get_date(self.request.GET.get('month', None))
        d = self.get_date(self.request.GET.get('month', None))
        calendrier_test = Calendar(d.year)
        
        if instructor:
            # You might want to map the 'cars' values to actual instructor names
            instructor_name = {
                'Omari': 'Omari',
                'Huynh': 'Huynh',
                'Crocfer': 'Crocfer',
                'MAKRI': 'MAKRI',
                'HMIDACH': 'HMIDACH',
                 'ZIANI': 'ZIANI',
                 'NOUMA': 'NOUMA',
                 'NHAILA':'NHAILA',
                 'LAMNAH': 'LAMNAH'

            }.get(instructor)
        else:
            instructor_name = self.request.user.username
            print(f"{self.request.POST} post object ")
            


      

        instructor = Formateur("x" , instructor_name, 'y')
        
        
        cache_key = f'modules_{instructor_name}'

        
        if cache_key in cache:
            #  print(self.request.session['modules'])
            #  serialized_data = self.request.session['modules']
             data_from_excel_file = cache.get(cache_key)
             print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
             
             
        
        else:
            pythoncom.CoInitialize()  # Pour initialiser COM si nécessaire (pour Excel) 
            file = cache.get("master_excel_file")
            
            test_excel_file = ExcelFile()
            test_excel_file.open_worksheet("DEV WEB", file)
            test_excel_file.get_formateur_worksheet(instructor.get_last_name()) 
            modules = test_excel_file.create_modules(file)
            # Convertir les modules en dictionnaires avant de les stocker dans la session
            # self.request.session['modules'] = modules
            cache.set(cache_key, modules)
            # cache.add('modules', modules)  
            # serialized_data = self.request.session['modules'] 
            data_from_excel_file = cache.get(cache_key)
            print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
        
       

        # Instanciation de la date actuelle ou de la date fournie par l'URL
        # d = self.get_date(self.request.GET.get('month', None))

        # Gestion du calendrier basé sur Excel
        # calendrier_test = Calendar(d.year)
        # test_excel_file = ExcelFile()
        # test_excel_file.open_worksheet("DEV WEB")
        # test_excel_file.get_formateur_worksheet("CROCFER")
        # dico_module = {}
        # for i in range(0,5):
        #     dico_module[i] = Module("Java", "2024-8-10 00:00:00", "2024-9-10 00:00:00", "Sessions Continues", [], []).to_dict()
        
        # module_json = json.dumps(dico_module)
        # print(module_json, type(module_json))
        # self.request.session['module_json'] = module_json
        # print(f"module_test en session : {self.request.session['module_json']}")
        # dico_deserialize = json.loads(self.request.session['module_json'])
        # print(dico_deserialize, type(dico_deserialize))
        # for key in dico_deserialize:
        #     module_reconstr = Module.from_dict(dico_deserialize[key])
        #     print(f'{module_reconstr.get_date_debut()}')
        # reconstr_module = Module.from_dict(dico_deserialize)
        # print(f"{reconstr_module.get_date_debut()}")
        
        # Check if modules are already in session
        # if 'modules' in self.request.session:
        # if 'modules' in cache:
        #     #  print(self.request.session['modules'])
        #     #  serialized_data = self.request.session['modules']
        #      data_from_excel_file = cache.get('modules')
        #      print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
            #  print(f"keys : {serialized_data.keys()}", type(serialized_data))
            #  print(f"values : {serialized_data.values()}",type(serialized_data.values()))
            #  print(f"{type(serialize_data)}")
            
            #  for key in serialized_data:  
            # #    print(f"key{key}", type(key))
            #    for k in serialized_data[key]:
            #     #    print(f"k : {k}", type(k))
            #        module_data = json.loads(serialized_data[key][k])
            #        print(f"module_data : {module_data}", type(module_data))
            #        reconstructed_module = Module.from_dict(module_data)
            #     #    print(f"reconstr_module : {reconstructed_module.get_date_debut()}")
            #        serialized_data[key][k] = reconstructed_module
                
                 
         
              
        #         # # Use the from_dict method to create a Module object
        #         # reconstructed_module = Module.from_dict(module_data)
        #         # print(f"reconstr_module : {reconstructed_module}")
        #         # serialized_data[key][v] = reconstructed_module
            
        # #         # print(reconstructed_module.__dict__)
 
        # else:  
        #     modules = test_excel_file.create_modules()
        #     # Convertir les modules en dictionnaires avant de les stocker dans la session
        #     # self.request.session['modules'] = modules
        #     cache.set('modules', modules)
        #     # cache.add('modules', modules)  
        #     # serialized_data = self.request.session['modules'] 
        #     data_from_excel_file = cache.get('modules')
        #     print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
            
            
        #     # print(f"{deserialized}", type(deserialized))
        #     for key in serialized_data:  
        #     #    print(f"module_data : {module_data}", type(module_data))
        #        for k in serialized_data[key]:
        #            module_data = json.loads(serialized_data[key][k])
        #         #    print(f"module_data : {module_data}", type(module_data))
        #            reconstructed_module = Module.from_dict(module_data)
        #            serialized_data[key][k] = reconstructed_module
            
        # else:
        #     # print(f"avant session serialized_data : {test_excel_file.create_modules()}")
        #     # print(type(test_excel_file.create_modules()))   
        #     self.request.session['modules']  = test_excel_file.create_modules()
        #     # print(f"dans le else{self.request.session['modules']}")  
        #     serialized_data = self.request.session['modules']
        # for key in serialized_data:
        #     for k in serialized_data[key]:
        #         module_data = json.loads(serialized_data[key][k])
        #         # Use the from_dict method to create a Module object
        #         reconstructed_module = Module.from_dict(module_data)
        #         serialized_data[key][k] = reconstructed_module.to_dict()
                
               
            
        
         # Ajouter des événements au calendrier en fonction des données Excel
        calendrier_test.dictionaries_module_to_calendar(data_from_excel_file)
        html_cal = calendrier_test.formatmonth(d.month)

        # Ajout du calendrier HTML au contexte
        context['calendar'] = mark_safe(html_cal)

        # Ajout des informations de navigation (mois précédent et suivant)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        return context

    def get_date(self, req_month):
        if req_month:
            year, month = (int(x) for x in req_month.split('-'))
            return date(year, month, 1)
        return datetime.today()

    def prev_month(self, d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        return 'month=' + str(prev_month.year) + '-' + str(prev_month.month)

    def next_month(self, d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        return 'month=' + str(next_month.year) + '-' + str(next_month.month)




# def test(request, *args, **kwargs):

#         dico = cache.get("blackClover")
#         print(f"dico : {dico}")
    
        
#         return render(request, 'calendartest.html',dico)
    


# def test2(request):
#     dico_test = {"Bonjour": "Igor", "Salut": "Nasser"}

#     cache.set("blackClover", dico_test, 10000)
#     print(cache.get("blackClover"))
    
#     return render(request, 'calendartest.html', dico_test)
    
# class CalendarDetailView(DetailView):
     
    
#      def find_module_by_id(module_id, dico):
#          for key in dico:
#              for k in dico[key]:
#                  if dico[key][k].get_id_module() == module_id:
#                     return dico[key][k]
    
#      def moduleinfo(self, request, module_id):           
#             modules = cache.get("modules")        
#             print(type(modules))        
#             module = self.find_module_by_id(module_id, modules)        
#             print(type(module))            
#             dico = module.to_dict()        
#             print(type(dico))        
#             dicocontext = {}        
#             dicocontext["module_dict"] = dico        
#             return render(request, "calendar_detail.html",dicocontext)   

  
class CalendarDetailView(DetailView):    
      def find_module_by_id(self, module_id, dico): 
          for key in dico:                
              for k in dico[key]:
                  if dico[key][k].get_id_module() == module_id: 
                      return  dico[key][k]  
                   
      def get(self, request, module_id):        
            modules = cache.get("modules")  
            print(type(modules))       
            module = self.find_module_by_id(module_id, modules)    
            print(type(module))       
            dico = module.to_dict()    
            print(type(dico))       
            dicocontext = {}       
            dicocontext["module_dict"] = dico       
            return render(request, "module_details.html",dicocontext)     


def personalspace(request):
     
     if  request.user.is_authenticated:
        messages.success(request, "the dinosaur codes better than you do!")

      
        
        
        return render(request, 'personal.html')
     
          
          
             
             

         
         