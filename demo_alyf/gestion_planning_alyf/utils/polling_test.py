
import requests
import time
from .file_upload_alyf import upload_excelfile_to_temp
from .verification import verifyallformateurs
import django
import os

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

def get_http_file_metadata(url, interval=30):
 



    response = requests.head(url)
    
  

    last_mod_time = response.headers.get('Last-Modified')


    while True:
                try: 
                      
                      time.sleep(interval)
                      response = requests.head(url)
                      current_mod_time = response.headers.get('Last-Modified')
                      if current_mod_time != last_mod_time:
                        print("changes incoming!")

                        upload_excelfile_to_temp()
                        verifyallformateurs()
                        
                        
                        #a la fin de cette etape, nous devrions avoir le nouveau fichier excel stocké sur notre serveur



                        
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

current_mod_time = get_http_file_metadata(url)
#print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {current_mod_time}")