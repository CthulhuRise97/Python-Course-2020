# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:23:45 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    tkinter.messagebox.showinfo("Título","Mensaje de la información")

boton = tkinter.Button(raiz,text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()