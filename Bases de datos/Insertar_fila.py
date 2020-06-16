# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:26:41 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES('Antonio','Perez','Gomez',35)")

conexion.commit()

conexion.close()