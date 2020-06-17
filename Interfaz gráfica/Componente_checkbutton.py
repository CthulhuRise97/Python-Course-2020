# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:19:55 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def verificar():
    valor = check.get()
    if(valor == 1):
        print("Check positivo")
    else:
        print("Check negativo")

check = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz,text="Opcion 1",variable=check,onvalue=1,offvalue=0,command=verificar)
boton1.pack()

raiz.mainloop()