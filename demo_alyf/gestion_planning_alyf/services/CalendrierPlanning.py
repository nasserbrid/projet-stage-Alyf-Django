import calendar

from django.http import HttpResponseRedirect
from requests import request
from . import Module
from . import ExcelFile
from datetime import datetime
from calendar import HTMLCalendar
from datetime import date
from django.urls import reverse


#https://stackoverflow.com/questions/42171990/create-a-one-month-calendar-with-events-on-it-in-python


# def redirect_to_module_info(uuid):
#     # ...
#     uuid = uuid
#     # ...
#     return HttpResponseRedirect(reverse("moduleinfo", args=(uuid,)))

class Calendar(HTMLCalendar):
    def __init__(self, year):
        self.year = year
        # self.yearcalendar  = calendar.Calendar().yeardatescalendar(year)
        self.yearcal  = calendar.Calendar().yeardatescalendar(year, width = 12)
       
        # self.yearcal  = calendar.Calendar().yeardayscalendar(2024)
      
        # print(self.yearcal)

        
        self.events =  [[[[] for day  in range(len(self.yearcal[0][i][j]))] 
           for j in range(len(self.yearcal[0][i]))] 
          for i in range(len(self.yearcal[0]))]
        
        super(Calendar, self).__init__()

     
    def _yearmonthday_to_index(self, month, day):
        'Trouver l’indice du jour dans un mois donné'
        print(f"month  and day in yearmonthday_to_index : {month}, {day}")
        target_date = date(self.year, month, day) # Créer un objet date
        
        for week_n, week in enumerate(self.yearcal[0][month - 1]):  # Chercher dans le mois correspondant
            try:
                i = week.index(target_date)
                return week_n, i
            except ValueError:
                pass
        raise ValueError(f"There aren't {target_date} in month {month}")
    
    # def _yearweek_to_index(self, week):
    #     'Trouver l’indice de la semaine dans un mois donné'
    #     target_date = date(self.monthdatescalendar(), week)  # Créer un objet date
    #     for  week in enumerate(self.monthdatescalendar()):  # Chercher dans la semaine correspondant
    #         try:
    #             i = week.index(target_date)
    #             print(i)
    #             return week, i
    #         except ValueError:
    #             pass
    #     raise ValueError(f"There aren't {target_date} in month {week}")


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



    def add_module_to_calendrier(self, module):
        
       dates =  module.extract_module_dates()
        
       for date in dates:
            self.add_event(int(date[5:7]), int(date[8:10]), {"id_module":module.get_id_module(), "nom_module":module.get_nom_module()})

       
    def formatday(self, day, month):
        if day != 0:
            events = self.get_events_for_day(month, day)
            
            d = ''
            
            for event in events:
                print(event)
                url = reverse('moduleinfo', args=[event['id_module']])
                d += f'<li><a href="{url}">  {event["nom_module"]}</a></li>'
                # d += f'<li><a href="{request.build_absolute_uri(reverse("calendar_detail", kwargs={"id_module": event["id_module"]}))}"> (id_module : {event["id_module"]}), (nom_module : {event["nom_module"]})</a></li>'
            if len(d) > 1:
                return f"<td class = 'aveccours' ><span class='date'>{day}</span><ul> {d} </ul></td>"
            else:
                return f"<td class = 'sanscours' ><span class='date'>{day}</span><ul> {d} </ul></td>"
                
         
          
        return '<td class="notinmonth"></td>'
     
    # def formatday(self, day, month):
    #     if day != 0:
    #         events = self.get_events_for_day(month, day)
            
    #         d = ''
            
    #         for event in events:
    #             print(event)
    #             url = reverse('moduleinfo', args=[event['id_module']])
    #             d += f'<li><a href="{url}">  {event["nom_module"]}</a></li>'
    #             # d += f'<li><a href="{request.build_absolute_uri(reverse("calendar_detail", kwargs={"id_module": event["id_module"]}))}"> (id_module : {event["id_module"]}), (nom_module : {event["nom_module"]})</a></li>'
    #             if len(d)>=10:

    #                 return f"<td class ='aveccours'><span class='date'>{day}</span><ul> {d} </ul></td>"
                
    #             else:
    #                 return f"<td class ='sanscours'><span class='date'>{day}</span><ul> {d} </ul></td>"
         
          
    #     return '<td></td>'
        	
        
            
            
            # d += f'<li> (event : {event}</li>'
            
        # if day != 0:
          
         
			
	 	 
    # formats a week as a tr 
    def formatweek(self, theweek, month):
        
        # theweek = self.monthdays2calendar(self.year, month)
        # week_ = self._yearweek_to_index(theweek)
        # week = ''.join(self.formatday(d, month) for (d, month) in theweek)
        week = ''
        # return f'<tr> {week} </tr>'
        
        # # for d, weekday in theweek:
        for d, weekday in theweek:
            # print(d, weekday)
            week += self.formatday(d, month)
        return f'<tr> {week} </tr>'
		
	     
    def formatmonth(self, month, withyear=True):
        
        gestion_planning_alyf = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        
        gestion_planning_alyf += f'{self.formatmonthname(self.year, month, withyear=withyear)}\n'
        gestion_planning_alyf += f'{self.formatweekheader()}\n'
        
        for week in self.monthdays2calendar(self.year, month):
            gestion_planning_alyf += f'{self.formatweek(week, month)}\n'
        gestion_planning_alyf += "</table>"
        return gestion_planning_alyf
        
   

        
        
		
			
			
		
