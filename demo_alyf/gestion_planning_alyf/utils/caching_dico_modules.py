
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

    # iterator = iter(dico)

    # newdico = {}

    #print(dico)

    # for u in range(3):
    #     val = next(iterator)
    #     newdico.update({val:dico[val]})

    


    # print(newdico)


    

    for instructor, file in dico.items():
        excel = ExcelFile( )
        print(instructor.get_last_name())
        excel.open_worksheet("DEV WEB", file)
        
        new_modules = excel.create_modules(file)
        cache_key = f'modules_{instructor.get_last_name()}'
        
        cache.set(cache_key, new_modules)
       



def update_dico_module_for_instructors(formateurs):
      
    dico = cache.get("dict_sheets_temp_storage")

    for formateur in formateurs:

  

  
        for key, value in dico.items():
             print(f"{key.get_last_name()}: key")
        # print(f"{formateur.get_last_name()}: formateur")
             if key.get_last_name() == formateur:
           
                fileA = dico[key]
            # print(f"{fileA}: file A" )
            # print(f"{fileA}: file A", type(fileA) )
            # cle = key
            # print(f"{cle}: cle" )




        cache_key = f'modules_{formateur}'
        excel = ExcelFile()
        excel.open_worksheet("DEV WEB", fileA)
        
        new_modules = excel.create_modules(fileA)
        cache.set(cache_key, new_modules)
    


    print(f"la liste des formateurs pour laquelle une modif a eu lieu est {formateurs}")


   

    
  


   
   


    

    # for instructor, file in dico.items():
    #     excel = ExcelFile( )
    #     print(instructor.get_last_name())
    #     excel.open_worksheet("DEV WEB", file)
        
    #     new_modules = excel.create_modules(file)
    #     cache_key = f'modules_{instructor.get_last_name()}'
        
    #     cache.set(cache_key, new_modules)


#create_temp_data_for_all_instructors()
        

        
