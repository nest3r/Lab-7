import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

list1 = [np.random.random() for _ in range(1000000)]
list2 = [np.random.random() for _ in range(1000000)]
array1 = np.array(list1)
array2 = np.array(list2)

start = time.perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end = time.perf_counter()
list_time = end - start

start = time.perf_counter()
result_array = np.multiply(array1, array2)
end = time.perf_counter()
array_time = end - start

print("Время выполнения для стандартного списка:", list_time)
print("Время выполнения для массива:", array_time)

data = pd.read_csv('data2.csv')

column_data = data.iloc[:, 3]

plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=20, color='black')
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=20, edgecolor='black', density=True, cumulative=True)
plt.title('Эквализированная гистограмма')
plt.xlabel('Значения')
plt.ylabel('Кумулятивная частота')

std_deviation = column_data.std()
print("Среднеквадратичное отклонение:", std_deviation)


x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
y = np.cos(x)
z = x / np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

ax.set_title('3D График')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')

plt.show()