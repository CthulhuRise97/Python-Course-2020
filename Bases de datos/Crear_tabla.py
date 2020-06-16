# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:21:48 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PERSONAS(nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

conexion.commit()

conexion.close()