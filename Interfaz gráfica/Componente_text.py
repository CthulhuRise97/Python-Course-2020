# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:09:24 2020

@author: Fernando García
"""


import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

entrada = tkinter.Text(raiz)
entrada.config(width=20,height=10,font=("Verdana",15),padx=10,pady=10,fg="green",selectbackground="lightgrey")
entrada.pack()

raiz.mainloop()