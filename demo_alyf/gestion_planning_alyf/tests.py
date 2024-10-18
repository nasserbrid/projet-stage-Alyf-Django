from django.test import TestCase
from .services.ExcelFile import ExcelFile
from .services.Formateur import Formateur
import unittest
import win32com.client
import os
import tempfile
import pathlib as pl
import pandas as pd
import re


#



class TestExcelFile(unittest.TestCase):
    def test_excel_com_object_creation(self):
        try:
            excel = win32com.client.Dispatch("Excel.Application")
            self.assertIsNotNone(excel)
            self.assertTrue(isinstance(excel, win32com.client.CDispatch))
            
            # Vérifier quelques propriétés ou méthodes pour s'assurer que c'est bien un objet Excel
            self.assertTrue(hasattr(excel, 'Workbooks'))
            #self.assertTrue(hasattr(excel.Workbooks, 'Sheets'))
            self.assertTrue(hasattr(excel, 'Visible'))
            
            # Nettoyer
            excel.Quit()
            del excel
        except Exception as e:
            self.fail(f"Échec de la création de l'objet COM Excel: {str(e)}")

    
    def test_open_worksheet(self):
        
        # Arrange
        excel = ExcelFile()
        excel.open_worksheet("DEV WEB")
        
   

        # Act
        used_range = excel.worksheet.UsedRange

        #Assert
        self.assertGreater(used_range.Rows.Count, 10)
        self.assertGreater(used_range.Columns.Count, 10)

    
    def test_save_formateur_worksheet(self):
        # Arrange
        excel = ExcelFile()
        formateur = Formateur("x", "Omari", "y")
        excel.open_worksheet("DEV WEB")
        excel.save_formateur_worksheet("Omari")
        

        # Arrange
        excel = ExcelFile()
        excel.open_worksheet("DEV WEB", os.getenv("ALYFDEVPATH"))
        formateur_name = excel.worksheet.Cells(1,8).Value

        #Assert
        
        self.assertEqual(formateur_name, formateur.get_last_name())

        
    def test_save_instructor_sheet_separately(self):
        # Arrange
        excel = ExcelFile()
        excel.open_worksheet("DEV WEB")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsm').name
        formateur_name = "toto"

         # Act
        excel.save_instructor_sheet_separately("toto", temp_file)
        path = pl.Path(temp_file)

        #Assert
        self.assertEqual(path.is_file(),  True)
        

       
    def test_create_fullYearTeachingDataFrame_from_instructorSheet(self):
         # Arrange
          excel = ExcelFile()
          excel.open_worksheet("DEV WEB")
          excel_path = os.getenv("ALYFDEVPATH")
        
          # Act
          path = pl.Path(excel_path)
          df = excel.create_fullYearTeachingDataFrame_from_instructorSheet(path)
          used_range = excel.worksheet.UsedRange

          #Assert
          self.assertEqual(path.is_file(), True)
          self.assertGreater(used_range.Rows.Count, 10)
          self.assertGreater(used_range.Columns.Count, 10)
         
          self.assertTrue(isinstance(df, pd.DataFrame))

        
    def test_create_modules(self):

        #Arrange 
          excel = ExcelFile()
          excel.open_worksheet("DEV WEB")
          excel_path = os.getenv("ALYFDEVPATH")
          path = pl.Path(excel_path)
          #df = excel.create_fullYearTeachingDataFrame_from_instructorSheet(path)

        #Act
          dicoval = excel.create_modules()
        #Assert
         # self.assertTrue(isinstance(liste_de_cours, list))
          self.assertTrue(isinstance(dicoval, dict))

    
    def test_find_session_type(self):
         #Arrange 
         excel = ExcelFile()
   

         #Act
         session_name = "Sessions Alternantes"
         session_type = excel.find_session_type(session_name)

         #Assert
         self.assertTrue(isinstance(session_name, str))
         self.assertTrue(isinstance(session_type, str))

    
    def test_get_session_dataframe(self):
         #Arrange 
        excel = ExcelFile()
        excel.open_worksheet("DEV WEB")
        excel.save_formateur_worksheet("Huynh")
        
         #Act
        correct_values_sheetname = ["Isitech - XEFI",  "Sessions Alternantes"]
        incorrect_values_sheetname = ["dsfjksdfj", "isitech"]
        correct_values_session_name = ["TSSR LY7 14102024 - ALT"]
        incorrect_values_session_name = ["sqdksqkd"]

        df1 =  excel.get_session_dataframe(correct_values_sheetname[1], correct_values_session_name[0])
       # df2 =  excel.get_session_dataframe(correct_values_sheetname[0], correct_values_session_name[0])

        #Assert
        self.assertTrue(isinstance(df1, pd.DataFrame))
        self.assertRaises(IndexError, excel.get_session_dataframe, correct_values_sheetname[0], correct_values_session_name[0])



    def test_create_list_cours_termines_et_futur(self):
         #Arrange
         excel = ExcelFile()
         excel.open_worksheet("DEV WEB")

         #Act
         correct_values_modulename = ["Scripting PowerShell", "Déploiement"]
         correct_values_sheetname = ["Isitech - XEFI",  "Sessions Alternantes", "Sessions Continues"]
         correct_values_session_name = ["PRF-TSSR AVIGNON 291123", "TSSR POLE EMPLOI ISI 041223 "]
         liste1 = excel.create_list_cours_termines_et_futur(correct_values_modulename[1], correct_values_sheetname[2], correct_values_session_name[0])
         liste2 = excel.create_list_cours_termines_et_futur(correct_values_modulename[0], correct_values_sheetname[2], correct_values_session_name[0])

         #Assert
         self.assertTrue(isinstance(liste1, tuple))
         self.assertTrue(isinstance(liste2, tuple))
         #self.assertRaises(IndexError, correct_values_modulename[1] , correct_values_sheetname[0], correct_values_session_name[0])
        

    def test_retrieve_instructor_list(self):
         #Arrange 
         excel = ExcelFile()
         email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      

         #Act 
         instructors =  excel.retrieve_instructor_list("FORMATEURS - MODULES")
         print(instructors)


         #Assert
         self.assertTrue(isinstance(instructors, list))
         for instructor in instructors:
            email = instructor[0] 
            self.assertTrue(re.match(email_regex, email))
            
         

    
              





    

    






    # def test_open_worksheet(self):
    
    # #Arrange
    #      excel = ExcelFile()

    # # Act 

    #      excel.open_worksheet()


    # #Assert 
    #      assert





