# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:44:02 2020

@author: Fernando García
"""


from datetime import datetime

fechayhora = datetime.now()
print(fechayhora)

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

hora = fechayhora.hour
minuto = fechayhora.minute
segundo = fechayhora.second
microsegundo = fechayhora.microsecond

print("{}:{}:{} del {}/{}/{}".format(hora,minuto,segundo,dia,mes,año))