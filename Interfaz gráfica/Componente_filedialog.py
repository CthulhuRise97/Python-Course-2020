# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:35:06 2020

@author: Fernando García
"""


import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

def abrirFichero():
    rutaFichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutaFichero)
    
boton = tkinter.Button(raiz,text="Pulsar para empezar",command=abrirFichero)
boton.pack()

raiz.mainloop()