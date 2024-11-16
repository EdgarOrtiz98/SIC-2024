import numpy as np

A = np.array([[1, -4],[-4, 1]])
B = np.array([[1, -8],[-8, 2]])

suma = A + B
resta = A - 0.5 * B
multiplicacion = 5 * A

print("A + B = \n", suma)
print("A - 0.5B = \n", resta)
print("5A = \n", multiplicacion)
