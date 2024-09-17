import calendar
from . import Module
from . import ExcelFile
from datetime import datetime
from datetime import date

#https://stackoverflow.com/questions/42171990/create-a-one-month-calendar-with-events-on-it-in-python

class Calendar:
    def __init__(self, year):
        self.year = year
        # self.yearcalendar  = calendar.Calendar().yeardatescalendar(year)
        self.yearcal  = calendar.Calendar().yeardatescalendar(year, width = 12)
       
        # self.yearcal  = calendar.Calendar().yeardayscalendar(2024)
      
        # print(self.yearcal)

        
        self.events =  [[[[] for day  in range(len(self.yearcal[0][i][j]))] 
           for j in range(len(self.yearcal[0][i]))] 
          for i in range(len(self.yearcal[0]))]

     
    def _yearmonthday_to_index(self, month, day):
        'Trouver l’indice du jour dans un mois donné'
        target_date = date(self.year, month, day)  # Créer un objet date
        for week_n, week in enumerate(self.yearcal[0][month - 1]):  # Chercher dans le mois correspondant
            try:
                i = week.index(target_date)
                return week_n, i
            except ValueError:
                pass
        raise ValueError(f"There aren't {target_date} in month {month}")

    def add_event(self, month, day, event_dict):
        'Ajouter un événement pour un jour spécifique'
        week, w_day = self._yearmonthday_to_index(month, day)
        self.events[month - 1][week][w_day].append(event_dict)

    def displayevents(self, month, day):
            week, w_day = self._yearmonthday_to_index(month, day)
            print(self.events[month - 1][week][w_day])

    def get_events_for_day(self, month, day):
        week, w_day = self._yearmonthday_to_index(month, day)
        return self.events[month - 1][week][w_day]
      
    

    def  dictionaries_module_to_calendar(self, dico):
        for key in dico:
            for k in dico[key]:
                print(f"nom module : {dico[key][k].get_nom_module()},id module : {dico[key][k].get_id_module()}")
                self.add_module_to_calendrier(dico[key][k])


    

    # def dictionaries_module_to_calendar2(self,dico):
    #     for key, value in dico.items():
    #         print(f"{key} key")
    #         print(f"{value} value")
            
                # self.add_module_to_calendrier(module)

           


    def add_module_to_calendrier(self, module):
        
       dates =  module.extract_module_dates()
        
       for date in dates:
            # print(type(date))
            # print(int(date[6:7]), int(date[8:]))
            # print(date)
            # print((date[5:7]), (date[8:10]))
            self.add_event(int(date[5:7]), int(date[8:]), {"id_module":module.get_id_module(), "nom_module":module.get_nom_module()})

           
     
    
        
