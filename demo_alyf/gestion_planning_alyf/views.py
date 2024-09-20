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
   
from .services.Module import Module
import json
from django.views import View
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .services.ExcelFile import ExcelFile
from .services.CalendrierPlanning import Calendar  # Ton calendrier personnalisé
from datetime import date, datetime, timedelta
import calendar
import pythoncom

class CombinedCalendarView(View):
    

    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'calendar.html', context)

    def get_context_data(self, **kwargs):
        context = {}
        pythoncom.CoInitialize()  # Pour initialiser COM si nécessaire (pour Excel)

        # Instanciation de la date actuelle ou de la date fournie par l'URL
        d = self.get_date(self.request.GET.get('month', None))

        # Gestion du calendrier basé sur Excel
        calendrier_test = Calendar(d.year)
        test_excel_file = ExcelFile()
        test_excel_file.open_worksheet("DEV WEB")
        test_excel_file.get_formateur_worksheet("HUYNH")
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
        if 'modules' in self.request.session:
            #  print(self.request.session['modules'])
             serialized_data = self.request.session['modules']
            #  print(f"serialize_data : {serialize_data}", type(serialize_data))
             print(f"keys : {serialized_data.keys()}", type(serialized_data))
             print(f"values : {serialized_data.values()}",type(serialized_data.values()))
            #  print(f"{type(serialize_data)}")
            
        for key in serialized_data:
            
            # print(f"module_data : {module_data}", type(module_data))
            for k in serialized_data[key]:
                 print(k, type(k))
                 module_data = json.loads(serialized_data[key][k])
                #  print(f"module_data : {module_data}", type(module_data))
                 reconstructed_module = Module.from_dict(module_data)
                #  print(f"reconstr_module : {reconstructed_module.get_date_debut()}")
                 serialized_data[key][k] = reconstructed_module.to_dict()
                
                
        #         # # Use the from_dict method to create a Module object
        #         # reconstructed_module = Module.from_dict(module_data)
        #         # print(f"reconstr_module : {reconstructed_module}")
        #         # serialized_data[key][v] = reconstructed_module
            
        # #         # print(reconstructed_module.__dict__)
 
        else:  
            modules = test_excel_file.create_modules()
            # Convertir les modules en dictionnaires avant de les stocker dans la session
            self.request.session['modules'] = {key: {k: json.dumps(module.to_dict()) for k, module in value.items()} for key, value in modules.items()}
            serialized_data = self.request.session['modules']       
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
        calendrier_test.dictionaries_module_to_calendar(serialized_data)
        html_cal = calendrier_test.formatmonth(d.month)

        # Ajout du calendrier HTML au contexte
        context['calendar'] = mark_safe(html_cal)

        # Ajout des informations de navigation (mois précédent et suivant)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        return 

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



