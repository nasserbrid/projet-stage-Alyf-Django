

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
from deepdiff import DeepDiff

from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()




def is_planning__change(instructor):
    #print(f"{instructor}: instructor")

    

    dico = cache.get("dict_sheets_temp_storage")
    print(f"{dico}: dico")
   
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
            #print(f"{fileA}: file A" )
           # print(f"{fileA}: file A", type(fileA) )
            cle = key
            # print(f"{cle}: cle" )
            
            # print(f"I am fileA :{fileA}")
            break
    
   # print(formateur.get_last_name()) 
   # print(formateur)  
    # print(f"{dico[cle]} : file A")
    # print(f"{cle} : cle")   
   
    # print("file A not in local")
    # print(f"{cle}: cle" )
    # print(f"{cle.get_last_name()}: cle qui correspond à un formateur" )

    if cle is None:
     
     newest_excel_file = cache.get("master_excel_file")
     #print(f"newest excel file {newest_excel_file}")
     temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
     
     dico.update({formateur: temp_file})
     excelfile.open_worksheet('DEV WEB', newest_excel_file) 
     
     excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
     cache.set("dict_sheets_temp_storage", dico)
     return False
    # print(f"new file for instuctor {key} added to the temp files") 

    else:
   
     newest_excel_file = cache.get("master_excel_file")
   
     fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name

     if os.path.exists(fileB):
      os.remove(fileB)
   
    excelfile.open_worksheet('DEV WEB', newest_excel_file)
    excelfile.save_instructor_sheet_separately(formateur.get_last_name(), fileB)

  

     

    # Convertir les fichiers Excel en CSV pour une comparaison plus fiable
    print("juste avant le pd.read excel")
    data_fileA = pd.read_excel(fileA, sheet_name='DEV WEB', engine='openpyxl')
    data_fileB = pd.read_excel(fileB, sheet_name='DEV WEB', engine='openpyxl')

    # .to_csv('fileB.csv', index=False)


    # Remplacer les NaN par des espaces
    data_fileA = data_fileA.fillna('')
    data_fileB = data_fileB.fillna('')

    # Convertir les objets datetime en chaînes de caractères
    def convert_dates(value):
        if isinstance(value, datetime):
             return value.strftime("%Y-%m-%d %H:%M:%S")
        return value
    
    # Appliquer la conversion sur toutes les colonnes
    #df = df.applymap(convert_dates) (cette expression est depreciée)
    data_fileA = data_fileA.map(convert_dates)
    data_fileB = data_fileB.map(convert_dates)

    # data_fileA = data_fileA.to_csv('fileA.csv', index=False)
    
    # data_fileB = data_fileB.to_csv('fileB.csv', index=False)

    # Convertir le DataFrame en JSON
    data_fileA= data_fileA.to_dict(orient='records')
    data_fileB= data_fileB.to_dict(orient='records')

    print("comparing jsonfiles ")


    print(data_fileA == data_fileB)

    print("end of comparing jsonfiles ")


    # Comparer les fichiers JSON
    diff = DeepDiff(data_fileA,data_fileB)
    print(diff)


    print("JSON files created for comparison")
    print("les deux fichiers utilisés pour la comparaison sont")
    print(fileA, fileB)

    if diff:
      os.remove(fileA)  # Les fichiers sont différents, supprimer fileA
      print(f"Les fichiers JSON sont différents. {fileA}: fileA a été supprimé.")
      dico[cle] = fileB
      cache.set("dict_sheets_temp_storage", dico)
      return True   
     
    else:
     os.remove(fileB)  # Les fichiers sont identiques, supprimer fileB
     print(f"Les fichiers JSON sont identiques. {fileB}: fileB a été supprimé.")
     return False
   

    # Comparer les fichiers CSV
    # if filecmp.cmp('fileA.csv', 'fileB.csv', shallow=False):
    #     # os.remove(fileB)
    #     # os.remove('fileA.csv')
    #     # os.remove('fileB.csv')
    #     print("Files are identical. Removed fileB")
    #     return False
    # else:
    #     # os.remove(fileA)
    #     # os.remove('fileA.csv')
    #     # os.remove('fileB.csv')
    #     print("Files are different. Removed fileA")
    #     dico[cle] = fileB
   
    #     cache.set("dict_sheets_temp_storage", dico)
    #     return True




def verifyallformateurs():
    excel = ExcelFile()
    instructors = excel.retrieve_instructor_list("FORMATEURS - MODULES")

    formateurs_a_updater = []

    for instructor in instructors:
        print(f"{formateurs_a_updater}: formateur a updater")
       
        print(f"{instructor} : instructor")
        
        if is_planning__change(instructor) == True:
           formateurs_a_updater.append(instructor[2])

        print(f"{formateurs_a_updater}: formateur a updater")
        
        # else:
        #    print("no change in planning")
       
      
    return formateurs_a_updater


#verifyallformateurs()
# #verifie_si_planning__change(["elmoutee", "EL MOUTEE", "EL MOUTEE"])







# # def verifychanges():
# #     dico = cache.get("dict_sheets_temp_storage")

# #     for key, value in dico:
# #         verifie_si_planning__change(key)

# import shutil
# import tempfile
# import os
# import django
# import filecmp
# import pandas as pd
# from django.core.cache import cache
# from ..services.Formateur import Formateur
# from ..services.ExcelFile import ExcelFile

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# # Initialiser Django
# django.setup()

# def is_planning__change(instructor):
#     # Récupération du dictionnaire de cache contenant les fichiers temporaires des formateurs
#     dico = cache.get("dict_sheets_temp_storage")
#     excelfile = ExcelFile()

#     formateur = Formateur(instructor[1], instructor[2], instructor[0])
#     cle = None

#     # Recherche du formateur dans le cache
#     for key, value in dico.items():
#         if key.get_last_name() == formateur.get_last_name():
#             fileA = dico[key]
#             cle = key
#             break

#     # Si aucun fichier temporaire n'existe pour ce formateur, on le crée
#     if cle is None:
#         newest_excel_file = cache.get("master_excel_file")
#         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
#         dico.update({formateur: temp_file})

#         excelfile.open_worksheet('DEV WEB', newest_excel_file)
#         excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
#         cache.set("dict_sheets_temp_storage", dico)

#         return False

#     # Si un fichier existe déjà, on en génère un nouveau pour comparaison
#     newest_excel_file = cache.get("master_excel_file")
#     fileB = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name

#     if os.path.exists(fileB):
#         os.remove(fileB)

#     excelfile.open_worksheet('DEV WEB', newest_excel_file)
#     excelfile.save_instructor_sheet_separately(formateur.get_last_name(), fileB)

#     # Comparaison des deux fichiers Excel en utilisant des DataFrames pandas
#     dfA = pd.read_excel(fileA, sheet_name='DEV WEB', engine='openpyxl')
#     dfB = pd.read_excel(fileB, sheet_name='DEV WEB', engine='openpyxl')

#     # Si les fichiers sont identiques, on supprime fileB
#     if dfA.equals(dfB):
#         os.remove(fileB)
#         print("Les fichiers Excel sont identiques. Aucune mise à jour nécessaire.")
#         return False
#     else:
#         # Si les fichiers sont différents, on supprime fileA et on met à jour le cache
#         os.remove(fileA)
#         print("Les fichiers Excel sont différents. Mise à jour nécessaire.")
#         dico[cle] = fileB
#         cache.set("dict_sheets_temp_storage", dico)
#         return True

# def verifyallformateurs():
#     excel = ExcelFile()
#     instructors = excel.retrieve_instructor_list("FORMATEURS - MODULES")
#     formateurs_a_updater = []

#     for instructor in instructors:
#         print(f"{formateurs_a_updater} : formateur à mettre à jour")
#         print(f"{instructor} : instructor")

#         if is_planning__change(instructor):
#            formateurs_a_updater.append(instructor)

#         print(formateurs_a_updater)

#     return formateurs_a_updater

# # Appel de la fonction pour vérifier tous les formateurs
# verifyallformateurs()


        
    








    
