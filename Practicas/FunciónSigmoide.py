# Importar Librerías
import numpy as np
import matplotlib.pyplot as plt

# Definir la Función Sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Inicializar los Parámetros
w = 0.5  # peso
b = -1   # sesgo

# Definir la Función de Predicción
def predict(x):
    z = w * x + b
    return sigmoid(z)

# Datos del ejercicio
study_hours = np.array([1, 2, 3, 4, 5, 6, 7])
results = np.array([0, 0, 0, 1, 1, 1, 1])

# Generar valores de predicción
study_hours_range = np.linspace(0, 7, 100)
predicted_probs = predict(study_hours_range)

# Calcular las probabilidades de aprobar para cada hora de estudio
study_hours_probs = predict(study_hours)

# Crear figura y ejes para el gráfico
fig, ax = plt.subplots()

# Visualizar el Modelo
ax.plot(study_hours_range, predicted_probs, label='Curva Sigmoide', color='blue')

# Añadir puntos de probabilidad con diferentes colores para aprobados y no aprobados
for i in range(len(study_hours)):
    color = 'green' if results[i] == 1 else 'red'
    ax.scatter(study_hours[i], study_hours_probs[i], color=color, zorder=5)
    ax.annotate(f'{study_hours_probs[i]:.2f}', (study_hours[i], study_hours_probs[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Añadir línea del umbral
ax.axhline(y=0.5, color='gray', linestyle='--', label='Umbral 0.5', zorder=0)

# Añadir etiquetas y leyendas
ax.set_title('Clasificación Binaria con Función Sigmoide')
ax.set_xlabel('Horas de Estudio')
ax.set_ylabel('Probabilidad de Aprobar')
ax.set_yticks(np.linspace(0, 1.2, 7))
ax.grid(True)

# Crear una leyenda personalizada con puntos circulares
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Aprobado'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='No Aprobado')
]
ax.legend(handles=legend_elements + ax.get_legend_handles_labels()[0], loc='upper left')

# Mostrar el gráfico con la leyenda
plt.show()

# Evaluación del Modelo
def evaluate_model(hours):
    prob = predict(hours)
    return 1 if prob >= 0.5 else 0

# Evaluar para 3 horas de estudio
hours = 3
result = evaluate_model(hours)
print(f'El estudiante con {hours} horas de estudio {"aprobará" if result == 1 else "no aprobará"} el examen.')