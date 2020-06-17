# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:04:55 2020

@author: Fernando García
"""


def multiplicar(n1,n2):
    return n1 * n2

resultado = multiplicar(3,7)
print(resultado)

import unittest

class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()