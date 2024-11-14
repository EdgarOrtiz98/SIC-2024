import numpy as np

# Crear la matriz 5x4 con las calificaciones de los estudiantes
calificaciones = np.array([
    [7, 8, 6, 5],
    [9, 7, 6, 8],
    [8, 5, 7, 9],
    [6, 7, 8, 7],
    [5, 4, 5, 6]
])

print("Matriz de calificaciones:")
print(calificaciones)

# Media por asignatura (columna)
media_asignatura = np.mean(calificaciones, axis=0)
print("Media por asignatura:", media_asignatura)

# Varianza por estudiante (fila)
varianza_estudiante = np.var(calificaciones, axis=1)
print("Varianza por estudiante:", varianza_estudiante)

# Desviación estándar de la matriz completa
desviacion_estandar = np.std(calificaciones)
print("Desviación estándar de la matriz completa:", desviacion_estandar)

# Valores únicos
valores_unicos = np.unique(calificaciones)
# Ordenar valores únicos
valores_ordenados = sorted(set(valores_unicos))
print("Valores únicos ordenados:", valores_ordenados)

# Filtrar estudiantes con calificaciones mayores a 6
estudiantes_filtrados = calificaciones[np.all(calificaciones > 6, axis=1)]
print("Estudiantes con calificaciones mayores a 6 en todas las asignaturas:")
print(estudiantes_filtrados)

# Reemplazar calificaciones menores o iguales a 6 por 10
calificaciones_modificadas = np.where(calificaciones <= 6, 10, calificaciones)
print("Matriz modificada con calificaciones <= 6 reemplazadas por 10:")
print(calificaciones_modificadas)

# Máximo, mínimo y mediana por asignatura
maximo_asignatura = np.max(calificaciones, axis=0)
minimo_asignatura = np.min(calificaciones, axis=0)
mediana_asignatura = np.median(calificaciones, axis=0)

print("Máximo por asignatura:", maximo_asignatura)
print("Mínimo por asignatura:", minimo_asignatura)
print("Mediana por asignatura:", mediana_asignatura)

# Resumen completo por asignatura
for i in range(calificaciones.shape[1]):
    print(f"Asignatura {i + 1}:")
    print(f"  Media: {media_asignatura[i]}")
    print(f"  Mediana: {mediana_asignatura[i]}")
    print(f"  Máximo: {maximo_asignatura[i]}")
    print(f"  Mínimo: {minimo_asignatura[i]}")
    print(f"  Valores únicos: {valores_ordenados}")