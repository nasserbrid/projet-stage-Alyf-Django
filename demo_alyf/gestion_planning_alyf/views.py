
import email

from django.http import Http404, HttpResponse
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
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 


from pathlib import Path
logger = logging.getLogger(__name__)





def home(request):
     
     if request.user.is_authenticated:
         
         #if user is_admin()
         #return redirect("selectformateur/")
         #else:
         #return redirect("calendar/")
        
        return redirect("selectformateur/")
  
     return render(request, 'home.html')


def selectformateur(request):

    pythoncom.CoInitialize()
    excel = ExcelFile()
    selectvalues = excel.retrieve_instructor_list("FORMATEURS - MODULES")
    names = []
    for instructor in selectvalues:
        names.append(instructor[2])

    print(selectvalues)
        
    return render(request, "selectformateur.html", {"selectvalues":names})


def telecharger_document(request, file):
        # f = Document.objects.filter(id = id).first()
        # files = cache.get("dict_sheets_temp_storage")
        # print(f"{files} files value")
        # formateur = cache.get("current_formateur")
        # print(f"{formateur} formateur value")
        # for key, value in files.items():
        #     if key.get_last_name() == formateur:
        #         file = files[key]
        #         print(f"{file}: file value")
                data = open(file, 'rb').read()
                username = request.session["current_formateur"]
                response = HttpResponse(data, content_type='application/vnd.ms-excel.sheet.macroEnabled.12')
                response["Content-Disposition"] = u"attachment; filename={0}.xlsm".format(username)
                return response
            # else:
            #  raise Http404      
    

class CalendarView(View):
    
    
    
    """_summary_
    """
    def get(self, request , *args, **kwargs):
       
        context = self.get_context_data()
        print("in get")
      
     
        return render(request, 'calendar.html', context)
    
    
    def post(self, request, *args, **kwargs):
        selected_instructor = request.POST.get('instructorname') 
        # cache.set("current_formateur", selected_instructor)
        self.request.session["current_formateur"] = selected_instructor
        context = self.get_context_data(instructor=selected_instructor)
        return render(request, 'calendar.html', context)

    """_summary_
    """
    def get_context_data(self, instructor=None, file=None ,**kwargs):
        context = {}
        d = self.get_date(self.request.GET.get('month', None))
        print(f"{d} : day in the get")
        # d = self.get_date(self.request.GET.get('month', None))
        calendrier_test = Calendar(d.year)
        
        if instructor:
            # You might want to map the 'cars' values to actual instructor names
            instructor_name = instructor
            print(f"{instructor} : instructor")
            print(f"{instructor_name} : instructor_name")
           
        elif self.request.session["current_formateur"] != None:
            #   instructor_name = cache.get("current_formateur")
              instructor_name = self.request.session["current_formateur"]
              print(f"{instructor_name} : instructor_name in the cache")

        else:
            instructor_name = self.request.user.username
            self.request.session["current_formateur"] = instructor_name
            print(f"{instructor_name} : instructor avec self.request.user.username")
            
            print(f"{self.request.POST} post object ")
            

        instructor = Formateur("x" , instructor_name, 'y')
        
        
        cache_key = f'modules_{instructor_name}'
        print(f"{cache_key} cache key value")

        
        if cache_key in cache:
            #  print(self.request.session['modules'])
            #  serialized_data = self.request.session['modules']
             data_from_excel_file = cache.get(cache_key)
             #print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
             print("found instructor in cache")
             
             
        
        else:
            pythoncom.CoInitialize()  # Pour initialiser COM si nécessaire (pour Excel) 

            if cache.get("master_excel_file") != None:
                file = cache.get("master_excel_file")
                test_excel_file = ExcelFile()
                test_excel_file.open_worksheet("DEV WEB", file)
                test_excel_file.get_formateur_worksheet(instructor.get_last_name()) 
                modules = test_excel_file.create_modules(file)
                cache.set(cache_key, modules)
                data_from_excel_file = cache.get(cache_key)
                print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))
            else:
                test_excel_file = ExcelFile()
                test_excel_file.open_worksheet("DEV WEB")
                test_excel_file.get_formateur_worksheet(instructor.get_last_name()) 
                modules = test_excel_file.create_modules()
                cache.set(cache_key, modules)
                data_from_excel_file = cache.get(cache_key)
                print(f"serialized_data : {data_from_excel_file}", type(data_from_excel_file))

            
            
        
         # Ajouter des événements au calendrier en fonction des données Excel
        calendrier_test.dictionaries_module_to_calendar(data_from_excel_file)
        html_cal = calendrier_test.formatmonth(d.month)

        # Ajout du calendrier HTML au contexte
        context['calendar'] = mark_safe(html_cal)

        # Ajout des informations de navigation (mois précédent et suivant)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        context['username'] = mark_safe(self.request.user.username)
        
        files = cache.get("dict_sheets_temp_storage")
        print(f"{files}: files values")
        print(f"{instructor_name}: instructor name")
        for key, value in files.items():
        
            if key.get_last_name()== instructor_name.upper()  :
                file = files[key]
            
                print(f"{file}: file value")
            # if key.get_last_name() ==  instructor_name :
                
                
                
            
        context['filename'] = file
        # context['file'] = self.telecharger_document()

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



    # def telecharger_document(self):
    #     # f = Document.objects.filter(id = id).first()
    #     files = cache.get("dict_sheets_temp_storage")
    #     print(f"{files} files value")
    #     formateur = cache.get("current_formateur")
    #     print(f"{formateur} formateur value")
    #     for key, value in files.items():
    #         if key.get_last_name() == formateur:
    #             file = files[key]
    #             print(f"{file}: file value")
    #             data = open(file, 'rb').read()
    #             response = HttpResponse(data, content_type='application/vnd.ms-excel.sheet.macroEnabled.12')
    #             response["Content-Disposition"] = u"attachment; filename={0}.md".format(file.name)
    #             return response
    #         else:
    #          raise Http404
              
                
         
    #     # if f is not None:
    #     #     my_file = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, "pdf", f.name)
    #     #     data = open(my_file, 'rb').read()
    #     #     response = HttpResponse(data, content_type='application/pdf')
    #     #     response["Content-Disposition"] = u"attachment; filename={0}.md".format(f.name)
    #     #     return response
    #     # else:
    #     #      raise Http404
     
  
class CalendarDetailView(DetailView):    
      def find_module_by_id(self, module_id, dico): 
          for key in dico:                
              for k in dico[key]:
                  if dico[key][k].get_id_module() == module_id: 
                      return  dico[key][k]  
                   
      def get(self, request, module_id): 
            # instructeur = cache.get("current_formateur") 
            instructeur = self.request.session["current_formateur" ]
            print('in the get method')
            print(instructeur)
            cache_key =  f'modules_{instructeur}'      
            modules = cache.get(cache_key)  
            print(f"{modules} modules")
            print(type(modules))       
            module = self.find_module_by_id(module_id, modules)    
            print(module)       
            dico = module.to_dict()    
            print(type(dico))       
            dicocontext = {}       
            dicocontext["module_dict"] = dico       
            return render(request, "module_details.html",dicocontext)     


def personalspace(request):
     
     if  request.user.is_authenticated:
        print(request.user)
        messages.success(request, "the dinosaur codes better than you do!")

      
        
        
        return render(request, 'personal.html')
     
          
          
             
             

         
         