import numpy as np
import matplotlib.pyplot as plt

# Определение функций
x = np.linspace(-np.pi, np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
z = np.tan(x)

# Первый график: две функции в одном окне
plt.figure(1)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('График функций sin(x) и cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Второй график: одна функция в отдельном окне
plt.figure(2)
plt.plot(x, z, label='tan(x)')
plt.title('График функции tan(x)')
plt.xlabel('x')
plt.ylabel('z')
plt.grid(True)
plt.legend()

plt.show()



