# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:32:13 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","¿Quieres borrar este fichero?")
    if(resultado == "yes"):
        print("Si, quiero borrar el fichero")
    else:
        print("No, no quiero borrar el fichero")
        
boton = tkinter.Button(raiz,text="Pulsar para preguntar",command=preguntar)
boton.pack()

raiz.mainloop()