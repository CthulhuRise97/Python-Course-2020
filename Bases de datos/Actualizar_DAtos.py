# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:43:32 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 30 WHERE nombre = 'Antonio'")

conexion.commit()

conexion.close()