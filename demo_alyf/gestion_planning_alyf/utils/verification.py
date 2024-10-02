

import tempfile
from ..services.Formateur import Formateur
from ..services.ExcelFile import ExcelFile

from django.core.cache import cache 
from md5_test import compare_excel_files, compute_file_md5
import os 


def verifie_si_planning__change(formateur, planning_origin, dernier_planning):

    dico = cache.get("dict_sheets_temp_storage")

    formateur = Formateur("x", formateur, "y")

    excelfile = ExcelFile()

    if dico.get(formateur.get_last_name()) == None:
         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm')
         dico.update(formateur.get_last_name(), temp_file.name) = temp_file.name
         excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
         return f"new file for instuctor {formateur} added to the temp files"
    
    fileA = dico.get(formateur.get_last_name())
    fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
    excelfile.open_worksheet('DEV WEB')
    excelfile.save_instructor_sheet_separately(formateur.get_last_name(),fileB)

    if compare_excel_files(fileA,fileB):
        os.remove(fileB)
    else:
        os.remove(fileA)
        del dico[formateur]
        dico.update(formateur.get_last_name(), fileB)
        cache.set("dict_sheets_temp_storage", dico)
        









        
        
        
        
        

    








    
