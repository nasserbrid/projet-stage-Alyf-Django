from django.test import TestCase
from .services.ExcelFile import ExcelFile
from .services.Formateur import Formateur
import unittest
import win32com.client
import os
import tempfile
import pathlib as pl
import pandas as pd


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
         


    # def test_open_worksheet(self):
    
    # #Arrange
    #      excel = ExcelFile()

    # # Act 

    #      excel.open_worksheet()


    # #Assert 
    #      assert





