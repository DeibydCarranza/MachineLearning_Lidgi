#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:49:54 2022

@author: monserratlopez
"""

#Usos básicos de numpy
 
import numpy as np

array = np.array([[1,2,3],[4,5,6]], dtype = np.int64)
print(array)
#Crea una matriz llena de unos, 3 filas 4 columnas
unos = np.ones((3,4))
print(unos)
#Crea una matriz de ceros
ceros = np.zeros((3,4))
print(ceros)

#Crear una matriz con valores aleatorios (filas,columnas)
aleatorios = np.random.random((2,2))
print(aleatorios)

#Crear una matriz vacia
vacia = np.empty((3,2))
print(vacia)
#Crear una matriz con un solo valor en todas las posiciones
full = np.full((2,2),8)
print(full)
#Crear matriz con valores espaciados uniformemente
espacio1 = np.arange(0,30,5) #(inicio,entre 0-30,# de valores)
print(espacio1)

espacio2 = np.linspace(0,2,5)
print(espacio2)

# Crear matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(4)
print(identidad2)

#INSPECCIONAR MATRICES
#Conocer las dimensiones de una matriz
a =np.array([(1,2,3),(4,5,6)])
print(a.ndim)
#Conocer el tipo de dato
print(a.dtype)
#Tamaño y forma de la matriz
print(a.size)
print(a.shape)

#Cambio de tamaño y forma de la matriz
b = np.array([(8,9,10),(11,12,13)])
#Tres columnas y 2 filas. A dos columnas y 3 filas
print(b)
#b = b.reshape(3,2)
print(b)
#Seleccionar un solo elemento de la matriz
#Fila cer columna 2
print(a[0,2])
#Valores de la columan 3
print(a[0:,2])
#OPERACIONES MATEMATICAS
#Minimo, máximo y suma
print(a.min())
print(a.max())
print(a.sum())
#Raíz cuadrada y desviación estandar
print(np.sqrt(a))
print(np.std(a))
#Suma, resta, multiplicación y división de matrices
print(a+b)
print(b-a)
print(a*b)
print(a/b)