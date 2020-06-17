# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:38:57 2020

@author: Fernando García
"""


class Saludos:
    """
    Esta clase tendrá dos funciones buenos_dias y adios
    Ambas funciones recibirán como parámetro un nombre
    """
    def buenos_dias(self,nombre):
        """ Esta funcion sirve para decir buenos dias a una persona """
        print("Buenos días {}".format(nombre))
    def adios(self,nombre):
        """ Esta funcion sirve para decir adios a una persona """
        print("Adios {}".format(nombre))