from django.shortcuts import render
from django.http import HttpResponse
from .services.ExcelFile import ExcelFile
from .services.Module import Module
from .services.CalendrierPlanning import Calendar
from datetime import time 
import time 
import win32com.client
import pandas as pd
from dotenv import load_dotenv

import pythoncom


load_dotenv() 






def affichercalendrier(request):
    # Exemple simple de lecture et d'affichage du planning
    calendrier_test = Calendar(2024)

    calendrier_test.add_event(12,8,{"id_module": 5, "nom_module": "Nasser et Igor"})

    calendrier_test.get_events_for_day(12,8)
    # calendrier_test.formatday(12,8)
    
    # calendrier_test.formatweek(3,12)
    
    event = calendrier_test.formatmonth(12)
    
    # event = calendrier_test.create_html_cal()

    
    return render(request, 'calendar.html', {'event': event})




def get_dicomodule(request):
    pythoncom.CoInitialize()
    
    
    test_excel_file = ExcelFile() 
    
  
    test_excel_file.open_worksheet("DEV WEB")
    test_excel_file.get_formateur_worksheet("HUYNH")
    data = test_excel_file.create_modules()
    # data = {"excel": test_excel_file}
    return render(request, "calendar.html", {'data':data})
   

