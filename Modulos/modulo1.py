# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:49:27 2020

@author: Fernando García
"""


class coche:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print("Marca: {}\nColor: {}\nCombustible: {}\nCilindrada: {}".format(self.marca,self.color,self.combustible,self.cilindrada))

media = lambda n1,n2,n3 : (n1+n2+n3)/3