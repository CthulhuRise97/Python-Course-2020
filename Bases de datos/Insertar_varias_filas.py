# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:28:50 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

lista_personas = [('Pedro','Rodriguez','Perez',26),('Maria','Lopez','Gomez',45),('Luis','Gonzales','Perez',46)]

cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)",lista_personas)

conexion.commit()

conexion.close()