
import tempfile
from ..services.Formateur import Formateur
from ..services.ExcelFile import ExcelFile

from django.core.cache import cache 
from .md5_test import compare_excel_files, compute_file_md5
import os 
import django
from ..services import ExcelFile,Formateur
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()




from django.contrib.auth.models import User
from django.contrib.auth.models import Group




def createallusers():
    excel = ExcelFile()
    instructors = excel.retrieve_instructor_list("FORMATEURS - MODULES")
    print(instructors)

    for instructor in instructors:
        User.objects.create_user(instructor[2], instructor[0], instructor[1])
        print("....")
    

    print("all users created")




def setadmins():

    groupe = Group.objects.get(name="administrateur")

    listeadmin = [("OMARI","youssef.omari@alyfpro.fr" ), ("BLANCHARD", "jolan.blanchard@alyfpro.fr"),("BLANCHARD", "quentin.blanchard@alyfpro.fr"),("BEN CHIKHA", "soukeina.benchikha@alyfpro.fr") ]

    for value in listeadmin:
        admin = User.objects.get(username=value[0])
        admin.groups.add(groupe)
    


    
    
    # for instructor in instructors:
    #     User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")




# user1 = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")



setadmins()