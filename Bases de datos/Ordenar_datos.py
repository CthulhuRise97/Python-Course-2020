# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:36:32 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

lista_ordenada = cursor.fetchall()

for persona in lista_ordenada:
    print(persona)

cursor.close()