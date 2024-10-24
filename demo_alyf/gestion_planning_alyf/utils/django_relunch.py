import subprocess
import time
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

def restart_django_app():
    # Spécifie le chemin vers ton script de gestion de serveur
    manage_py_path = os.path.join(os.getenv("PATH_PROJECT"), "manage.py")
    
    while True:
        try:
            # Lance l'application Django
            process = subprocess.Popen(['python', manage_py_path, 'runserver', '0.0.0.0:8000'], creationflags=subprocess.CREATE_NO_WINDOW)
            print("Django application started. PID:", process.pid)
             

            # Attends que le processus se termine
            process.wait()

            # Si le processus se termine, attends un moment avant de relancer
            print("Django application crashed. Restarting in 5 seconds...")
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred: {e}")
            break
        
        
restart_django_app()