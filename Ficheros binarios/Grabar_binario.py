# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:38:36 2020

@author: Fernando García
"""


import pickle

lista_colores = ["azul","verde","rojo","amarillo"]

fichero = open("fichero_colores.pckl","wb")

pickle.dump(lista_colores,fichero)

fichero.close()