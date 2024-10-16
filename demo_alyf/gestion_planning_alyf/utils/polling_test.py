
import requests
import time
from .file_upload_alyf import upload_excelfile_to_temp
from .verification import verifyallformateurs
from .caching_dico_modules import update_dico_module_for_instructors
import django
import os

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

def get_http_file_metadata(url, interval=60):
 

    print("hello world i am running in the get http metadata function")

  
        


    response = requests.head(url)
    
    print(response.__dict__)

    last_mod_time = response.headers.get('Last-Modified')


    while True:
        try:
              
              
                      
              time.sleep(interval)
           
              response = requests.head(url)
              
              current_mod_time = response.headers.get('Last-Modified')
              if current_mod_time != last_mod_time:
                print("changes incoming!")

                upload_excelfile_to_temp()
                formateurs_a_updater = verifyallformateurs()
                update_dico_module_for_instructors(formateurs_a_updater)

                
                print(f"New Modification Time: {current_mod_time}")
                last_mod_time = current_mod_time

              else:
                   print("no modifications yet")

        except Exception as e:
              print(f"An error occurred: {e}")
              break
        
             


    
    return current_mod_time

# URL of the file
url = 'http://localhost:8080/alyf.xlsm'

print("ligne 79")
current_mod_time = get_http_file_metadata(url)
#print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {current_mod_time}")