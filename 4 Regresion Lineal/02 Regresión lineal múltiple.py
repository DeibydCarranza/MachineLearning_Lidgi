# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Se importan las librerías a utilizar
from sklearn import datasets, linear_model

#Importamos los datos de la misma librería de scikit-learn
boston = datasets.load_boston()
print(boston)

#Verifica la información contenida en el dataset
print('Información contenida en el dataset:')
print(boston.keys())
print()

#Verifica las características del dataset
print('Caracaterísticas del dataset:')
print(boston.DESCR)

#Verifica la cantidad de datos que hay en el dataset
print('Cantidad de datos:')
print(boston.data.shape)
print()

#Verifica la información de las columnas
print('Nombre columnas:')
print(boston.feature_names)

######## Preparar la data regresión lineal múltiple ##############

#Seleccionamos las columnas 5,6,7 del dataset
X_multiple = boston.data[:, 5:8]
print(X_multiple)

#Definimos los datos correspondientes a las etiquetas
y_multiple = boston.target

############ Implementación de regresión lineal múltiple ############

from sklearn.model_selection import train_test_split

#Separar los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple,y_multiple,test_size=0.2)

#Definimos el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#Entrenamos el modelo
lr_multiple.fit(X_train,y_train)

#Realizar una predicción
Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
print()

print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)

print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)

print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train)) 
























































































