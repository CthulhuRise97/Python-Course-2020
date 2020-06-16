# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:50:24 2020

@author: Fernando García
"""

import pickle

frutas = {"manzana":"apple", "naranja":"orange","platano":"banana","limon":"lemon"}

fichero = open("frutas.pckl","wb")

pickle.dump(frutas,fichero)

fichero.close()