Le texte ci dessous est issu de l'IA Boot.Dev et correspond àu texte généré en réponse à la question : Comment récupurérer uniquement les métadonnées d'un fichier distant.




Using SFTP with pysftp

If you have SFTP access:

import pysftp

def get_remote_file_metadata(host, username, private_key, remote_path):
    with pysftp.Connection(host, username=username, private_key=private_key) as sftp:
        # Retrieve the file attributes
        file_attrs = sftp.stat(remote_path)
        
        # Access metadata from file attributes
        file_size = file_attrs.st_size
        modification_time = file_attrs.st_mtime

    return file_size, modification_time

# Remote connection details
host = 'remote.server.com'
username = 'your_username'
private_key = '/path/to/your/private_key'
remote_path = '/path/to/remote/excelfile.xlsx'

file_size, mod_time = get_remote_file_metadata(host, username, private_key, remote_path)
print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {mod_time}")

Explanation

    sftp.stat(remote_path): Retrieves metadata such as size (st_size) and last modification time (st_mtime) without downloading the file.

Using HTTP/HTTPS

If the file is accessible via HTTP and supports HEAD requests:

import requests

def get_http_file_metadata(url):
    response = requests.head(url)
    file_size = response.headers.get('Content-Length')
    mod_time = response.headers.get('Last-Modified')

    return file_size, mod_time

# URL of the file
url = 'http://example.com/path/to/excelfile.xlsx'

file_size, mod_time = get_http_file_metadata(url)
print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {mod_time}")
Using SFTP with pysftp

If you have SFTP access:

import pysftp

def get_remote_file_metadata(host, username, private_key, remote_path):
    with pysftp.Connection(host, username=username, private_key=private_key) as sftp:
        # Retrieve the file attributes
        file_attrs = sftp.stat(remote_path)
        
        # Access metadata from file attributes
        file_size = file_attrs.st_size
        modification_time = file_attrs.st_mtime

    return file_size, modification_time

# Remote connection details
host = 'remote.server.com'
username = 'your_username'
private_key = '/path/to/your/private_key'
remote_path = '/path/to/remote/excelfile.xlsx'

file_size, mod_time = get_remote_file_metadata(host, username, private_key, remote_path)
print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {mod_time}")

Explanation

    sftp.stat(remote_path): Retrieves metadata such as size (st_size) and last modification time (st_mtime) without downloading the file.

Using HTTP/HTTPS

If the file is accessible via HTTP and supports HEAD requests:

import requests

def get_http_file_metadata(url):
    response = requests.head(url)
    file_size = response.headers.get('Content-Length')
    mod_time = response.headers.get('Last-Modified')

    return file_size, mod_time

# URL of the file
url = 'http://example.com/path/to/excelfile.xlsx'

file_size, mod_time = get_http_file_metadata(url)
print(f"File Size: {file_size} bytes")
print(f"Last Modified Time: {mod_time}")
