# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:34:10 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad > 40")

personas = cursor.fetchall()

for persona in personas:
    print(persona)
    
conexion.close()