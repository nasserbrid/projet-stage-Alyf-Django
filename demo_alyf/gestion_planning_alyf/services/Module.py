#import ExcelFile
import uuid
import pandas as pd
import json
from datetime import datetime,date, timedelta
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 


class Module:
    def __init__(self, nom_module, date_debut, date_fin,  session, modules_termines, modules_a_venir):
         self.__id_module = uuid.uuid4()
         self.__nom_module = nom_module
         self.__date_debut = datetime.strptime(str(date_debut),'%Y-%m-%d')
         self.__date_fin = datetime.strptime(str(date_fin),'%Y-%m-%d')
         self.__session = session
         self.__modules_termines = modules_termines
         self.__modules_a_venir = modules_a_venir
                   

     
    def get_id_module(self):
            return self.__id_module

    def get_nom_module(self):
            return self.__nom_module
        
    def get_date_debut(self):
            return self.__date_debut
        
    def get_date_fin(self):
             return self.__date_fin
        
    def get_session(self):
            return self.__session
        
    def get_modules_termines(self):
             return self.__modules_termines
        
    def get_modules_a_venir(self):
             return self.__modules_a_venir
    
    
    def set_nom_module(self, value):
            self.__nom_module = value
        
    def set_date_debut(self, value):
            self.__date_debut = value
        
    def set_date_fin(self, value):
            self.__date_fin = value
        
    def set_session(self, value):
            self.__session = value
        
    def set_modules_termines(self, value):
             self.__modules_termines = value
        
    def set_modules_a_venir(self, value):
             self.__modules_a_venir = value
    


#     #Définir une méthode qui permet d'utiliser le dataframe et qui va récupérer des sessions dans "DEV WEB"
#     def create_fullYearTeachingDataFrame_from_instructorSheet(self):
           
#            excel_path = os.getenv("ALYFDEVPATH")
           
#            #output_path = os.getenv("ALYFJSONPATH")
               
           
#            try:
#                   i=0 
#                   df_fullYearTeachingData = pd.read_excel(excel_path, sheet_name="DEV WEB", header=None,  usecols=[i,i+1,i+2], skiprows=3, index_col=None)
#                   df_fullYearTeachingData = df_fullYearTeachingData.fillna('')
               
                              
#            except FileNotFoundError:
#                    print("Le fichier Excel est introuvable.")
#                    exit(1)
#            except ValueError:
#               print('La feuille "DEV WEB" est introuvable.')
#               exit(1)
                  
#            for month in range(2,13):
#                    i +=3
#                    df = pd.read_excel(excel_path, sheet_name="DEV WEB", header=None, usecols=[i, i+1, i+2], skiprows=3, index_col=None)
#                    df = df.fillna('')
                                           
#            # Convertir les objets datetime en chaînes de caractères
#         #    def convert_dates(value):
#         #         if isinstance(value, datetime):
#         #             return value.strftime("%Y-%m-%d %H:%M:%S")
#         #         return value
       
           
#            # Renommer les colonnes de df2 pour qu'elles correspondent à celles de df1
#                    df.columns = df_fullYearTeachingData.columns
#                    #print(f"{df_fullYearTeachingData.columns} df1 colums")

           
#            # Concaténation des deux DataFrames verticalement
#                    df_fullYearTeachingData = pd.concat([df_fullYearTeachingData, df])
         

#           # Réinitialisation de l'index si nécessaire
#                    df_fullYearTeachingData.reset_index(drop=True, inplace=True)
       


#       # Affichage du résultat
#                    pd.set_option('display.max_rows', None)
#            #print(concat)
#                    df_fullYearTeachingData.dropna(subset=[0],  inplace= True)
#                    #df_fullYearTeachingData = df_fullYearTeachingData.map(convert_dates)
      
#            return df_fullYearTeachingData
           
#        # Récupération des modules
#                    #print(f"les valeurs unique sont :{df_fullYearTeachingData[1].unique()}")
        
#            """Cette partie est à l'utilisation de la classe Calendar_Planning   
#         # # Convertir le DataFrame en JSON
#         #    df_fullYearTeachingData = df_fullYearTeachingData.to_dict(orient='records')
#         #    #print(df1[0].keys())


#         # # Sauvegarder les données au format JSON
#         #    with open(output_path, 'w', encoding='utf-8') as json_file:
#         #            json.dump(df_fullYearTeachingData, json_file, ensure_ascii=False, indent=4, default="str")
#         #            print(f"Les données ont été exportées avec succès vers {output_path}")
#            """          
     
#      #Pour des raisons de lisibilité, nous utiliserons une autre méthode pour transformer nos données en JSON.            

#     def create_module(self):
#             #cette methode permettra de recuperer toutes les infos du module
#             #On récupère les modules
            
#            df  = self.create_fullYearTeachingDataFrame_from_instructorSheet()
           

#            liste_de_cours = df[1].unique()

#            for cours in liste_de_cours:
#                   print(cours)
#                   dates = df.index[df[1]==cours]
#                   dates_vals = []
#                   for date in dates:
#                          dates_vals.append(date)
#                   print(dates_vals)

#                   blocks = [[dates_vals[0]]]

#                   for i in range(1,len(dates_vals)):
#                          if dates_vals[i] - dates_vals[i-1] == 1:
#                                 blocks[-1].append(dates_vals[i])
#                          else:
#                                 blocks.append([])
#                                 blocks[-1].append(dates_vals[i])
#                   print(blocks)
                    
                     
           
    def extract_module_dates(self):
            
           date_debut = self.get_date_debut()
           print(type(date_debut))
           date_fin = self.get_date_fin()
           delta = timedelta(days=1)
           dates = []
          

           while date_debut <= date_fin:
    # add current date to list by converting  it to iso format
              dates.append(date_debut.isoformat())
        #       dates.append(date_debut.strftime('%Y-%m-%d'))
              print(type(date_debut))
    # increment start date by timedelta
              date_debut += delta
           print('Dates between', date_debut, 'and', date_fin)
           print(dates)
           return dates 
        #dates doit etre un tableau de chaine de characteres de dates au format iso
        #    dates = [date for date in date(date_debut, date_fin)]
        #    print(dates)
                    
            
        #     return self.get_id_module, , self.get_date_fin
            
      



# difference between current and previous date


# store the dates between two dates in a list





            
            

    def getInfo(self):
        print(f"Le module est {self.get_nom_module()}, \n  la date de debut est {self.get_date_debut()}, \n la date de fin est {self.get_date_fin()}, \n il a appartient a la session {self.get_session()} \n il etait précédé de {self.get_modules_termines()} \n et sera suivi de {self.get_modules_a_venir()}") 

                  
        