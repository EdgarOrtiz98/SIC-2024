import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = 3x + 1
def f(x):
    return 3 * x + 1

# Define the range for x values
x_values = np.linspace(-10, 10, 100)
y_values = f(x_values)

# Points to add
points_x = [-1/3, 0]
points_y = [0, 1]

# Plotting the function
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$f(x) = 3x + 1$', color='blue', linewidth=1.5)
plt.scatter(points_x, points_y, color='black', marker='o')

# Annotate points with exact values
plt.annotate("(-1/3, 0)", (-1/3, 0), textcoords="offset points", xytext=(-20,-10), ha='center', color='black')
plt.annotate("(0, 1)", (0, 1), textcoords="offset points", xytext=(10,5), ha='center', color='black')

# Labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función $f(x) = 3x + 1$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Set limits for a cleaner look
plt.xlim(-2, 2)
plt.ylim(-1, 3)
plt.legend()

# Show the plot
plt.show()