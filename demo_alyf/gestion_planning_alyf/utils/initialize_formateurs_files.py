import hashlib
from django.core.cache import cache 

import tempfile

import os
import django

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

from ..services import ExcelFile,Formateur








def build_schedule_files_for_formateurs(listofinstructors):

    formateurs = []

    # excelfile = ExcelFile()
    # excelfile.open_worksheet("DEV WEB")
    print("past open worksheet")

    for personne in listofinstructors:
        formateurs.append(Formateur("x", personne,"y"))


   

# Suppose you have a list of instructors


# Create a dictionary to store the temporary file paths
    directory_of_individual_instructor_sheet_in_temp_storage = {}

# Create a unique temporary file for each instructor
    for formateur in formateurs:
         excelfile = ExcelFile()
         excelfile.open_worksheet("DEV WEB")
         print(excelfile.open_worksheet("DEV WEB"))
         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
         directory_of_individual_instructor_sheet_in_temp_storage[formateur] = temp_file
         excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
    # cache.set("dict_sheets_temp_storage", directory_of_individual_instructor_sheet_in_temp_storage)
    print(directory_of_individual_instructor_sheet_in_temp_storage)
    cache.set("dict_sheets_temp_storage", directory_of_individual_instructor_sheet_in_temp_storage)


# Now you can refer to each instructor's temp file through the dictionary
# for instructor, file_path in temp_files.items():
#     print(f"The temporary file for {instructor} is located at: {file_path}")

    
   
build_schedule_files_for_formateurs(["Jolan", "Crocfer"])      