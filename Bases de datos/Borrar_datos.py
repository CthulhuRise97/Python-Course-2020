# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:41:22 2020

@author: Fernando García
"""


import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Luis'")

conexion.commit()

cursor.close()