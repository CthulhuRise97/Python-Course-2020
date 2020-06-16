# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:40:31 2020

@author: Fernando García
"""


import pickle

fichero = open("fichero_colores.pckl","rb")

lista_leida_fichero = pickle.load(fichero)

print(lista_leida_fichero)