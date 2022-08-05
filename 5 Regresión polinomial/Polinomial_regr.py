# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 09:42:37 2022

@author: David
"""

########## LIBRERÍAS A UTILIZAR ##########

import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

########## PREPARAR LA DATA ##########

boston = datasets.load_boston()
#print(boston)
print()

########## ENTENDIMIENTO DE LA DATA ##########

#Información contenida en el dataset
print('Información en el dataset:')
print(boston.keys())
print()

#Características del dataset
print('Características del dataset:')
print(boston.DESCR)

#Cantidad de datos que hay en los dataset
print('Cantidad de datos:')
print(boston.data.shape)
print()

#Informnación en las columnas
print('Nombres de las columnas:')
print(boston.feature_names)
print()

########## PREPARAR LA DATA REGRESIÓN POLINOMIAL ##########

#Trabajamos con la columna 6 del dataset
X_p = boston.data[:, np.newaxis, 5]

#Datos correspondientes a las etiquetas
y_p =  boston.target

#Graficas
plt.scatter(X_p, y_p)
plt.show()

########## IMPLEMENTACIÓN DE REGRESIÓN POLINOMIAL ##########

from sklearn.model_selection import train_test_split

#Separar los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)

from sklearn.preprocessing import PolynomialFeatures

#Se defineel grado del polinomio
poli_reg = PolynomialFeatures(degree = 2)

#Transformar las acaracterísticas existentes en características de mayor grado
X_train_poli = poli_reg.fit_transform(X_train_p) 
X_test_poli = poli_reg.fit_transform(X_test_p)

#Definir el algoritmo a utilizar
pr = linear_model.LinearRegression()

#Entrenar el modelo
pr.fit(X_train_poli, y_train_p)

#Realizar una predicción
Y_pred_pr = pr.predict(X_test_poli)

#Graficamos los  datos junto con el modelo
plt.scatter(X_test_p, y_test_p)
plt.plot(X_test_p, Y_pred_pr, color='red',linewidth=3)
plt.show()

print()
print('DATOS DEL MODELO REGRESIÓN POLINOMIAL')
print()

print('Valor de la pendiente o coeficiente "a":')
print(pr.coef_)

print('Valor de la intersección o coeficiente "b":')
print(pr.intercept_)

print('Presición del modelo:')
print(pr.score(X_train_poli, y_train_p))





















