import numpy as np

matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print('El elemento en la primera fila, primera columna: ',matriz[0,0])
print('El elemento en la segunda fila, tercera columna: ',matriz[1,2])

print('Primera fila: ',matriz[0])
print('Segunda fila: ',matriz[:,1])
print('Submatriz (filas 1 y 2, columnas 1 y 2: /n)',matriz[0:2,0:2])