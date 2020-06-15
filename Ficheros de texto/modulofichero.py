# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:11:54 2020

@author: Fernando García
"""

class Fichero:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def leer_fichero(self):
        fichero = open(self.nombre,"rt")
        datos_fichero = fichero.read()
        return datos_fichero
    
    def grabar_fichero(self,texto):
        fichero = open(self.nombre,"wt")
        fichero.write(texto)
        fichero.close()
    
    def incluir_fichero(self,texto):
        fichero = open(self.nombre,"at")
        fichero.write(texto)
        fichero.close()