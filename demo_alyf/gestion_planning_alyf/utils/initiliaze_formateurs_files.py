import hashlib
from django.core.cache import cache 

import tempfile


from gestion_planning_alyf.services.Formateur import Formateur
from gestion_planning_alyf.services.ExcelFile import ExcelFile





def build_schedule_files_for_formateurs(listofinstructors):

    formateurs = []

    excelfile = ExcelFile()
    excelfile.open_worksheet("DEV WEB")

    for personne in listofinstructors:
        formateurs.append(Formateur("x", personne,"y"))


   

# Suppose you have a list of instructors


# Create a dictionary to store the temporary file paths
    directory_of_individual_instructor_sheet_in_temp_storage = {}

# Create a unique temporary file for each instructor
    for formateur in formateurs:
         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm')
         directory_of_individual_instructor_sheet_in_temp_storage[formateur] = temp_file.name
         excelfile.save_instructor_sheet_separately(formateur.get_last_name(), temp_file)
    cache.set("dict_sheets_temp_storage", directory_of_individual_instructor_sheet_in_temp_storage)


# Now you can refer to each instructor's temp file through the dictionary
# for instructor, file_path in temp_files.items():
#     print(f"The temporary file for {instructor} is located at: {file_path}")

    
   
        