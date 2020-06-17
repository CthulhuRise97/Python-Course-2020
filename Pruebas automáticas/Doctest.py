# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:55:52 2020

@author: Fernando García
"""


def sumar(n1,n2):
    """
    
    Documentacion de la funcion "sumar".
    
    Recibe dos números como parámetros y devuelve su suma.
    >>> sumar(1,2)
    3
    
    >>> sumar(-1,4)
    3
     
    >>> sumar(-1,-2)
    -3
    
    """
    return n1 + n2;

resultado = sumar(3,2)
print(resultado)

import doctest
doctest.testmod()