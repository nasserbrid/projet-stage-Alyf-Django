
from django.core.cache import cache

import os
import django
from ..services import ExcelFile,Formateur
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

def create_temp_data_for_all_instructors():

    dico = cache.get("dict_sheets_temp_storage")
   
    #print(dico)

    iterator = iter(dico)

    newdico = {}

    #print(dico)

    for u in range(3):
        val = next(iterator)
        newdico.update({val:dico[val]})

    


    print(newdico)


    

    for instructor, file in newdico.items():
        excel = ExcelFile( )
        print(instructor.get_last_name())
        excel.open_worksheet("DEV WEB", file)
        
        new_modules = excel.create_modules(file)
        cache_key = f'modules_{instructor.get_last_name()}'
        
        cache.set(cache_key, new_modules)
       


create_temp_data_for_all_instructors()
        

        
