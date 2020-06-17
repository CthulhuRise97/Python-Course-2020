# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:16:33 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

entrada1 = tkinter.Entry(raiz)
entrada1.config(justify="center")
entrada1.pack()

entrada2 = tkinter.Entry(raiz)
entrada2.config(justify="center",show="*")
entrada2.pack()

raiz.mainloop()