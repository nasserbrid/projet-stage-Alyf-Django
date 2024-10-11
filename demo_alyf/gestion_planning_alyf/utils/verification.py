

import shutil
import tempfile
from ..services.Formateur import Formateur
from ..services.ExcelFile import ExcelFile

from django.core.cache import cache 
from .md5_test import compare_excel_files, compute_file_md5
import os 
import django
import filecmp
from ..services import ExcelFile,Formateur
import pandas as pd 
import openpyxl
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()




def verifie_si_planning__change(instructor):
    print(instructor)

    

    dico = cache.get("dict_sheets_temp_storage")
    print(dico)
   
    # dico.pop("Crocfer")
    # print(f" is Crocfer in dico? {dico["Crocfer"]}")
    
    excelfile = ExcelFile()

    formateur = Formateur(instructor[1], instructor[2], instructor[0])
   
    print(formateur.get_last_name())
    #instructeur pos 1  correspond a prenom, 2 a nom et 0 a email.
   # print(formateur.get_last_name())
    cle = None
    for key, value in dico.items():
        print(f"{key.get_last_name()}: key")
        # print(f"{formateur.get_last_name()}: formateur")
        if key.get_last_name() == formateur.get_last_name():
           
            fileA = dico[key]
            print(f"{fileA}: file A" )
            print(f"{fileA}: file A", type(fileA) )
            cle = key
            print(f"{cle}: cle" )
            
            # print(f"I am fileA :{fileA}")
            break
    
   # print(formateur.get_last_name()) 
   # print(formateur)  
    # print(f"{dico[cle]} : file A")
    # print(f"{cle} : cle")   
    if "fileA"  not in locals() :
     
     print("file A not in local")


    
     
     newest_excel_file = cache.get("master_excel_file")
     print(f"newest excel file {newest_excel_file}")
     temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
     
     dico.update({formateur: temp_file})
     excelfile.open_worksheet('DEV WEB', newest_excel_file) 
     excelfile.save_instructor_sheet_separately(key.get_last_name(), temp_file)
     cache.set("dict_sheets_temp_storage", dico)
     print(f"new file for instuctor {key} added to the temp files") 

    else:
        print(f"{fileA}: file A Soukeina Test ")

        print("in the else")
        
        newest_excel_file = cache.get("master_excel_file")
        print(f"newest excel file {newest_excel_file}")

        with open(tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm')) as fileB:
             excelfile.open_worksheet('DEV WEB', newest_excel_file)
             excelfile.save_instructor_sheet_separately(formateur.get_last_name(),fileB.name)



        # fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm')
        # print(fileB.closed)
        # # fileB.close()
        # print(fileB.closed)
        # print("trying to figure out if file b is open?")
        # print(f"{fileB}  file B")
        # print(f"{type(fileB)}  type file B")

        # fileB = dico[cle]
        # excelfile.open_worksheet('DEV WEB', newest_excel_file)
        # excelfile.save_instructor_sheet_separately(formateur.get_last_name(),fileB.name)
       
        # fileA.close()
        # fileB.close()
        print(fileA, fileB)

        #xlsm_dataA = pd.read_excel(fileA, sheet_name='DEV WEB', engine='openpyxl')
       # xlsm_dataB = pd.read_excel(fileB, sheet_name='DEV WEB', engine='openpyxl')

        print("past the pd.readexcel")

        #xlsm_dataA.to_csv('output.csv', index=False, header=True)
        #xlsm_dataB.to_csv('output1.csv', index=False, header=True)

        # compare_excel_files(fileA, fileB)


       # result = filecmp.cmp("output.csv", "output1.csv", shallow=False)
        #print(f"{result} : result")
       

        # fileB = fileA.copy()
        if compare_excel_files(fileA, fileB): 
             os.remove(fileB)
             #lorsqu'on compare fileA et fileB dans le if
             # on est supposé avoir fileA == fileB

             print("remove fileB")
        else:
            #lorsqu'on compare fileA et fileB dans le else
             # on est supposé avoir fileA != fileB
             os.remove(fileA)
             print("remove fileA")
             del dico[cle]
            #  dico.update(formateur.get_last_name(), fileB)
             print(f"{dico} : avant maj")
             print("\n\n")
             dico.update({formateur:fileB})
             print("\n\n")
             print(f"{dico} : après maj")
             cache.set("dict_sheets_temp_storage", dico)  

   

            

            
    

    
           
        

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


# def verifyallformateurs(liste_nom_famille):
#     for nom in liste_nom_famille:
#         verifie_si_planning__change(nom)



def verifyallformateurs():
    excel = ExcelFile()
    instructors = excel.retrieve_instructor_list("FORMATEURS - MODULES")

    for instructor in instructors:

        verifie_si_planning__change(instructor)


verifyallformateurs()
#verifie_si_planning__change(["elmoutee", "EL MOUTEE", "EL MOUTEE"])







# def verifychanges():
#     dico = cache.get("dict_sheets_temp_storage")

#     for key, value in dico:
#         verifie_si_planning__change(key)



        
        
        
        
        

    








    
