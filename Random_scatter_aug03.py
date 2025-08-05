# Rndom_scatter_aug03
import numpy as np
import matplotlib.pyplot as plt

n0_arr = 10   # количество точек
n1_arr = 15
n2_arr = 20

# ------- array-0 круги ---------
m0_x = 1.5*np.random.rand(n0_arr)
m0_y = 1.5*np.random.rand(n0_arr)

# ------- array-1  квадраты ---------
d1_ones = np.ones(n1_arr)
d1_x = np.random.rand(n1_arr)    # массив из n1_arr
d1_y = np.random.rand(n1_arr)    # массив из n1_arr
# сдвигаем набор точек
m1_x = 1.5*d1_x + 3*d1_ones
m1_y = 1.5*d1_y + 2*d1_ones

# ------- array-2 треугольники ---------
d2_ones = np.ones(n2_arr)
d2_x = np.random.rand(n2_arr)    # массив из n2_arr
d2_y = np.random.rand(n2_arr)    # массив из n2_arr
m2_x = 1.5*d2_x + 1*d2_ones
m2_y = 1.5*d2_y + 4*d2_ones

plt.scatter(m0_x, m0_y)              # круги
plt.scatter(m1_x, m1_y, marker="s")  # квадраты
plt.scatter(m2_x, m2_y, marker="^")  # треугольники

plt.title("Диаграмма рассеяния для трёх случайных наборов")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
