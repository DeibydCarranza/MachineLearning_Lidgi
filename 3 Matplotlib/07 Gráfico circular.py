# -*- coding: utf-8 -*-
"""
Creación de un gráfico circular por medio de Matplotlib

@author: David
"""
import matplotlib.pyplot as plt

#Definir los datos
dormir = [7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar = [7,8,7,2,2]
recreacion = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir', 'Comer', 'Trabajar', 'Recreación']
colores = ['red', 'purple', 'blue', 'orange']

#Conmfigurar las características del gráfico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90,
        shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

#Definir título
plt.title('Grafico circular')

#Mostrar figura
plt.show()