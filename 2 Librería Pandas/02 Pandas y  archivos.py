# -*- coding: utf-8 -*-
"""
Lectura y manipulación de archivos con Pandas

@author: David
"""
import pandas as pd


df = pd.read_csv('Animales.csv')
print('\t\tDataFrame original'.upper())
print(df)
#----------------------------------

#Verificar si hay datos nulos en el DataFrame
print('\n\t\tDatos nulos en el DataFrame'.upper())
print(df.isnull())

#----------------------------------
#Suma de datos nulos en el  DataFrame
print('\n\t\tSuma de datos nulos en el DataFrame'.upper())
print(df.isnull().sum())

#----------------------------------
#Limpieza de valores perdidos
print('\n\t\tLimpiando elementos con valores nulos'.upper())
print(df.dropna())
#print('\n\t\tEliminando las columnas donde haya datos vacíos'.upper())
#print(df.dropna(axis=1))

#----------------------------------
#Rellenar valores vacíos (si es que los hay)
print('\n\t\tRellenando valores vacíos'.upper())
print('Con 0:')
print(df.fillna(0)) #con 0
print('---------------')
print('Con la media:')
print(df.fillna(df.mean())) #con la media
