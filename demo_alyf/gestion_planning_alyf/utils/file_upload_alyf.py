import requests
import tempfile
from django.core.cache import cache

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_alyf.settings')

# Initialiser Django
django.setup()

# Téléchargement du fichier
url = 'http://localhost:8080/alyf.xlsm'
response = requests.get(url)

# Création d'un fichier temporaire avec un suffixe .xlsm
def upload_excelfile_to_temp():
    url = 'http://localhost:8080/alyf.xlsm'
    destination = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name

    cache.set("master_excel_file", destination)

# Écriture des données dans le fichier temporaire
    with open(destination, 'wb') as temp_file:
        temp_file.write(response.content)

# Se référer au fichier temporaire pour traitement
# Vous pouvez remplacer cette partie par le traitement spécifique que vous souhaitez effectuer
    # with open(destination, 'rb') as file:
    # # Effectuer des opérations sur le fichier
    #     data = file.read()
    #     print(f"Data size: {len(data)} bytes")  # Exemple, indique la taille des données

# Le fichier temporaire persiste jusqu'à ce que vous le supprimiez
    # print(f"The temporary file is available at: {destination}")


