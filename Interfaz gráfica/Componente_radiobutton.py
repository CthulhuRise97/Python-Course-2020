# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:14:14 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def seleccion():
    print("La opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz,text="Opcion 1",variable=opcion,value=1,command=seleccion)
botonradio1.pack()

botonradio2 = tkinter.Radiobutton(raiz,text="Opcion 2",variable=opcion,value=2,command=seleccion)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz,text="Opcion 3",variable=opcion,value=3,command=seleccion)
botonradio3.pack()

raiz.mainloop()