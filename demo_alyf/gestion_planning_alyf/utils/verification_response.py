from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from requests import request
import requests
from .django_relunch import restart_django_app

url = "http://localhost:8000/calendar/"

# response = requests.head(url)
# print(f"{response} : response")

def relance_si_pas_de_reponse():
    
    try :
        response = requests.head(url)
        print("i am running !")
        
    
    except Exception as e:
        restart_django_app()
    finally :
        print("le test a eu lieu !")
    
    
relance_si_pas_de_reponse()