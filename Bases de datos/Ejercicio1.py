# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:49:38 2020

@author: Fernando García
"""


import sqlite3

def crear_base(nombre):
    conexion = sqlite3.connect(nombre)
    conexion.close()

def crear_tabla(nombre):
    conexion = sqlite3.connect(nombre)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE Productos(id INTEGER, nombre TEXT, precio INTEGER)")
    conexion.commit()
    conexion.close()
    
def insertar_productos(nombre):
    conexion = sqlite3.connect(nombre)
    cursor = conexion.cursor()
    lista_productos = [('1','Impresora',300),('2','Raton',20),('3','Ordenador',600)]
    cursor.executemany("INSERT INTO Productos VALUES(?,?,?)",lista_productos)
    conexion.commit()
    conexion.close()

def consulta(nombre):
    conexion = sqlite3.connect(nombre)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()

    for producto in productos:
        print(producto)
        
    conexion.close()

nombre = "basededatos.db"
crear_base(nombre)
crear_tabla(nombre)
insertar_productos(nombre)
consulta(nombre)