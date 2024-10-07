

import tempfile
from ..services.Formateur import Formateur
from ..services.ExcelFile import ExcelFile

from django.core.cache import cache 
from .md5_test import compare_excel_files, compute_file_md5
import os 
import django
from ..services import ExcelFile,Formateur
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()




def verifie_si_planning__change(formateur):

    

    dico = cache.get("dict_sheets_temp_storage")
    print(dico)
   
    # dico.pop("Crocfer")
    # print(f" is Crocfer in dico? {dico["Crocfer"]}")
    
    excelfile = ExcelFile()

    formateur = Formateur("x", formateur, "y")
   # print(formateur.get_last_name())
    cle = None
    for key, value in dico.items():
        if key.get_last_name() == formateur.get_last_name():
           
            fileA = dico[key]
            cle = key
            # print(f"I am fileA :{fileA}")
            break
    
        
    if "fileA"  not in locals() :
    
     
     newest_excel_file = cache.get("master_excel_file")
     print(f"newest excel file {newest_excel_file}")
     temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
     dico.update({formateur: temp_file})
     excelfile.open_worksheet('DEV WEB', newest_excel_file) 
     excelfile.save_instructor_sheet_separately(key.get_last_name(), temp_file)
     cache.set("dict_sheets_temp_storage", dico)
     print(f"new file for instuctor {key} added to the temp files") 

    else:
        
        newest_excel_file = cache.get("master_excel_file")
        print(f"newest excel file {newest_excel_file}")
        fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
        excelfile.open_worksheet('DEV WEB', newest_excel_file)
        excelfile.save_instructor_sheet_separately(formateur.get_last_name(),fileB)
        print(fileA, fileB)

        # compare_excel_files(fileA, fileB)







   
        if compare_excel_files(fileA, fileB):
             os.remove(fileB)
             print("remove fileB")
        else:
             os.remove(fileA)
             print("remove fileA")
             del dico[cle]
            #  dico.update(formateur.get_last_name(), fileB)
             dico.update({formateur:fileB})
             cache.set("dict_sheets_temp_storage", dico)  

   

            

            
    print("Booyah")

    
           
        

    # excelfile = ExcelFile()

    # for key in dico.items():
    #     print(dico[key])
     


     
    # if dico.get(formateur.get_last_name()) == None:
    #      temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm')
    #      dico.update({formateur.get_last_name(): temp_file.name}) 
    #      excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
    #      return f"new file for instuctor {formateur} added to the temp files"
    
    # fileA = dico.get(formateur.get_last_name())
    # fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
    # excelfile.open_worksheet('DEV WEB')
    # excelfile.save_instructor_sheet_separately(formateur.get_last_name(),fileB)

    # if compare_excel_files(fileA,fileB):
    #     os.remove(fileB)
    # else:
    #     os.remove(fileA)
    #     del dico[formateur]
    #     dico.update(formateur.get_last_name(), fileB)
    #     cache.set("dict_sheets_temp_storage", dico)
        


# verifie_si_planning__change("Huynh")


def verifyallformateurs(liste_nom_famille):
    for nom in liste_nom_famille:
        verifie_si_planning__change(nom)








# def verifychanges():
#     dico = cache.get("dict_sheets_temp_storage")

#     for key, value in dico:
#         verifie_si_planning__change(key)



        
        
        
        
        

    








    
