# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:12:31 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def accion():
    print("Hola mundo")
    
boton = tkinter.Button(raiz,text="Ejecutar",command=accion)
boton.pack()

raiz.mainloop()