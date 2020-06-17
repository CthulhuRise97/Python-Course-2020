# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:08:35 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

frame = tkinter.Frame(raiz)
frame.config(bg = "blue",width = 400,height = 300)
frame.pack()

raiz.mainloop()