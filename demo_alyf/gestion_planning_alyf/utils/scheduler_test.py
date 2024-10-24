from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .verification_response import relance_si_pas_de_reponse
# from demo_alyf.gestion_planning_alyf.utils import verification_response

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(relance_si_pas_de_reponse, 'interval', minutes=1)
    scheduler.start()
    
start()