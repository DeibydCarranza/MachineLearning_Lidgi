#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 09:39:37 2022

@author: monserratlopez
"""
#VECTORES DE SOPORTE
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

###Preparar la data###
boston = datasets.load_boston()
print(boston)
print()
###Entrenamiento de la data  

#Verifico la inoformacion contenida en el datset

print('Caracteristicas del data set:')
print(boston.DESCR)

#Verifico la cantidad de datos que hay en los data set
print('Cantidad de datos:')
print(boston.data.shape)
print()

#Verifica la información de las columnas
print('Nombre columnas:')
print(boston.feature_names)

### PREPARAR LA DATA VERCTORES DE SOPORTE DE REGRESION

#Seleccionamos solamenete la columna 6 del dataset
X_svr = boston.data[:,np.newaxis,5]

print(X_svr)
#Defino los datos correspndientes a la etiquetas
y_svr = boston.target

print(y_svr)
#Graficamos los datos correspondientes a las etiquetas
plt.scatter(X_svr,y_svr)
plt.show()

#IMPLEMENTACION DE VECTORES DE SOPORTE DE REGRESION

from sklearn.model_selection import train_test_split

#Separo los datos de "Train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test, y_train, y_test = train_test_split(X_svr, y_svr,test_size=0.2)

from sklearn.svm import SVR

#Defino el algoritmo a utilizar

#svr = SVR(kernel = "linear",C = 1.0, epsilon = 0.2)
#Si se borra la configuracion del SVR pueden mejorar los resultados
svr = SVR()
#Entreno el modelo

svr.fit(X_train,y_train)

#Realizo una prediccion

Y_pred = svr.predict(X_test)

#Graficamos los datos junto con el modelo

plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color = "red", linewidth = 3)
plt.show()


print()
print("Datos del modelo vectores de soporte regresion")
print()

print("Presisición del modelo:")
#Score devuelve el resultado de la estadistica de R^2
print(svr.score(X_train, y_train))




























  
#


