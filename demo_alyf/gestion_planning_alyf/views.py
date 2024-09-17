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

    calendrier_test.add_event(12,8,"Nasser et Igor vont passer leur examen final")

    event = calendrier_test.get_events_for_day(12,8)

    
    
    return render(request, 'calendar.html', {'event': event})




# def get_dicomodule(request):
#     pythoncom.CoInitialize()
#     EXCEL = win32com.client.Dispatch("Excel.Application")
#     ExcelFile.EXCEL.Visible = True
#     test_excel_file = ExcelFile()
#     test_excel_file.open_worksheet("DEV WEB")
#     modules_data = test_excel_file.get_formateur_worksheet("HUYNH")
    
#     # # Récupérer les données sous forme de modules
#     # modules_data = test_excel_file.create_modules()
    
#     # Passer les données de manière structurée au template
#     return render(request, "calendar.html", {'modules': modules_data})

def get_dicomodule(request):
    pythoncom.CoInitialize()
    
    
    test_excel_file = ExcelFile() 
    
    # module = Module()
   
    # print(test_excel_file)
    test_excel_file.open_worksheet("DEV WEB")
    test_excel_file.get_formateur_worksheet("HUYNH")
    data = test_excel_file.create_modules()
    # data = {"excel": test_excel_file}
    return render(request, "calendar.html", {'data':data})
    #  dicotest = {"test":"test"}
    #  print("echo croissant sandwhich")
    #  EXCEL = win32com.client.Dispatch("Excel.Application")
    #  #EXCEL.visible = True

    #  return render(request, "calendar.html", dicotest )

