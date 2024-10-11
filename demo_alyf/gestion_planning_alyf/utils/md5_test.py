import hashlib
import hmac
from django.core.cache import cache 
from ..services.ExcelFile import ExcelFile
from ..services.Formateur import Formateur



def compute_file_md5(file_path, chunk_size=8192):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def compare_excel_files(file1_path, file2_path):
    # Compute MD5 hash for both files
    file1_hash = compute_file_md5(file1_path)
    print(file1_hash)
    
    file2_hash = compute_file_md5(file2_path)
    print(file2_hash)
    # print(hmac.compare_digest(file1_hash, file2_hash))
    
    # Compare hashes
    return file1_hash == file2_hash










            
           
        




# Example usage
# file1_path = 'C:\\Users\\iggdu\\pythonExperiments\\pickletest\\fichiers_excel_md5_tests\\alyfDataResult.xlsm'
# file2_path = 'C:\\Users\\iggdu\\pythonExperiments\\pickletest\\fichiers_excel_md5_tests\\aaaa.xlsm'

# if compare_excel_files(file1_path, file2_path):
#     print("The Excel files are the same.")
# else:
#     print("The Excel files have changed.")


