# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:12:37 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

texto = "Hola mundo"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()