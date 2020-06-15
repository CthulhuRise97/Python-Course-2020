# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:38:26 2020

@author: Fernando García
"""


import camelcase

camel = camelcase.CamelCase()

texto = "luis fernando garcia castañeda"

print(camel.hump(texto))