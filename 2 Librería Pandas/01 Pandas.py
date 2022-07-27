#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:09:51 2022

@author: monserratlopez
"""

#PANDAS

import numpy as np
import pandas as pd
#Le pasamos el array al data Frame
#------------------------------------
"""
data = np.array([['','Col1','Col2'],['Final',11,22],['Final2',33,44]])
print(pd.DataFrame(data = data[1:,1:], index = data[1:,0], columns = data[0,1:]))

"""
#------------------------------------

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame:')
print(df)

#------------------------------------
#Creando una serie
"""
series = pd.Series({"Argentina":"Buenos Aires", "Chile":"Santiago de Chile","Colombia":"Bogotá","Perú":"Lima"})
print ('Series:')
print(series)
"""
#Altura del DataFrame

print('Altura del DataFrame:')
print(len(df.index))

#Forma del Data Frame
print ('Forma del DataFrame:')
print(df.shape)

#Estadísticas del DataFrame
print ('Estadísticas del DataFrame:')
print(df.describe())

#Media de las columnas DataFrame
print('Media de las columnas DataFrame')
print(df.mean())

#Cuentas los datos del DataFrame
print('conteo de los Datos de DataFrame')
print(df.count())
#Valor más alto de cada columna de DataFrame
print('Valor más alto de cada columna de DataFrame')
print(df.max())

#Valor minimo de cada columna de DataFrame
print('Valor minimo de la columna de DataFrame')
print(df.min())
#Mediana de cada columa del DataFrame
print("Mediana de la columna del DataFrame")
#Valor más alto de cada columna de DataFrame
print('Valor más alto de cada columna de DataFrame')
print(df.median())
#Desviacion estandar de cada columna del DF
print('Desviacion estandar de cada columna del DF')
print(df.std())
#Seleccionar la primera columna del dataFrame
print("Primera columna del DataFrame")
print(df[0])
#Seleccionar 2 columnas del dtaFrame
print('Dos columnas del DataFrame:')
print(df[[0,1]])
#Seleccionar el valor de la primera fila y última columna del DataFrame
print('Valor de la primera fila y última columna del DataFrame')
print(df.iloc[0][2])
#Seleccionar los valores de la primea fila del DataFrame
print("valores de la primera fila del DataFrame:")
print(df.loc[0])
#or
print("valores de la primera fila del DataFrame:")
print(df.iloc[0,:])
