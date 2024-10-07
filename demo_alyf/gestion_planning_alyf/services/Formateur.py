import uuid
from . import ExcelFile
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

class Formateur:
    def __init__(self, first_name, last_name, email):
        self.__id = uuid.uuid4()
        self.__first_name = first_name 
        self.__last_name = last_name 
        self.__email = email 
    
   
    #def isConnect(self):
        
    #Getter
    def get_last_name(self):
        return self.__last_name
    
    #Setter
    def set_last_name(self, name):
        self.__last_name = name


    def consulter_planning(self,sheetName):
        file = ExcelFile.ExcelFile()
        file.open_worksheet(sheetName)
        file.get_formateur_worksheet(self.get_last_name())

        
        


    