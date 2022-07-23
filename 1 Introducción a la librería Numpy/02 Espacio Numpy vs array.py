#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:29:53 2022

@author: monserratlopez
"""

#Código que muestra el uso de espacio entre Numpy y una lista común
import numpy as np
import sys
S = range (1000)
print ('Resultado lista de Python:')
print (sys.getsizeof(5)*len(S))
print()
D = np.arange(1000)
print('Resultado NumPy Array: ')
print(D.size*D.itemsize)