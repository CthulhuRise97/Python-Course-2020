# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:51:22 2020

@author: Fernando García
"""


import pickle

fichero = open("frutas.pckl","rb")

lista_leida_fichero = pickle.load(fichero)

print(lista_leida_fichero)

print(lista_leida_fichero.values())