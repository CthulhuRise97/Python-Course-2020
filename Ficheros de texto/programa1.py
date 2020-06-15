# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:24:57 2020

@author: Fernando García
"""

import modulofichero as mf

nombre = "fichero_ejercicio.txt"

fichero = mf.Fichero(nombre)

texto = "este texto es ejemplo del ejercicio"
fichero.grabar_fichero(texto)

texto2 = "\nrenglon dos del fichero ejercicio"
fichero.incluir_fichero(texto2)

texto_res = fichero.leer_fichero()
print(texto_res)