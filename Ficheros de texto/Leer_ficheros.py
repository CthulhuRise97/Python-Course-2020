# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:56:47 2020

@author: Fernando García
"""

#Abrir un fichero
fichero = open("Fichero_ejemplo.txt","rt")
datos_fichero = fichero.read()
print(datos_fichero)

#Grabar un fichero (sobreescribir)
fichero = open("Fichero_ejemplo.txt","wt")
texto_de_fichero = "linea grabada en el fichero"
fichero.write(texto_de_fichero)
fichero.close()

#incluir linea al fichero
fichero = open("Fichero_ejemplo.txt","at")
texto_de_fichero2 = "\nlinea grabada bajo el fichero"
fichero.write(texto_de_fichero2)
fichero.close()

#borrar un fichero
import os
os.remove("Fichero_ejemplo.txt")