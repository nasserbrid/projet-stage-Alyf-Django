from ..services.ExcelFile import ExcelFile
from django.core.cache import cache
from ..services.Formateur import Formateur
import os

def create_temp_data_for_all_instructors(formateurliste):

    dico = cache.get("dict_sheets_temp_storage")

    excel = ExcelFile()

    instructorlist = []

    for formateur in formateurliste:
        instructorlist.append(Formateur("x", formateur, "y"))

    

    for instructor in instructorlist:
        excel.open_worksheet("DEV WEB", dico[instructor.get_last_name()])
        new_modules = excel.create_modules()
        cache_key = f'modules_{instructor.get_last_name()}'
        
        cache.set(cache_key, new_modules)
       

        

        
