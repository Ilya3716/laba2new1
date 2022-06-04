from Task_6 import *
import time, numpy as np, matplotlib.pyplot as plt, random as r

matrix_size = []
t_sq = []
t1_sq = []
t_trans = []
t1_trans = []
t_det = []
t1_det = []

def nash(func, array):
    start_time = time.perf_counter()
    func(array, i, i)
    end_time = time.perf_counter()
    return end_time - start_time

def nenash(func, array, degree=None):
    new_array = []
    for _ in array:
        line = []
        for l in _:
            line.append(l)
        new_array.append(line)
    if degree is not None:
        start_time = time.perf_counter()
        func(new_array, degree)
        end_time = time.perf_counter()
    else:
        start_time = time.perf_counter()
        func(new_array)
        end_time = time.perf_counter()
    return end_time - start_time


for i in range(2, 7):
    matrix = []
    matrix_size.append(i)
    for j in range(i):
        line = []
        for k in range(i):
            line.append(r.randint(1, 5))
        matrix.append(line)
    t_sq.append(nash(squared, matrix))
    t_det.append(nash(det, matrix))
    t_trans.append(nash(transpon, matrix))
    t1_sq.append(nenash(np.linalg.matrix_power, matrix, 2))
    t1_det.append(nenash(np.linalg.det, matrix))
    t1_trans.append(nenash(np.transpose, matrix))

fig, axs = plt.subplots(1, 3)
axs[0].set_title("Квадрат",fontsize = 12)
axs[0].set_xlabel("Размер матрицы")
axs[0].set_ylabel("Время выполнения")
axs[0].plot(matrix_size, t1_sq, label="Функция из NumPy")
axs[0].plot(matrix_size, t_sq, label="Функция из Task_6")

axs[1].set_title("Определитель",fontsize = 12)
axs[1].set_xlabel("Размер матрицы")
axs[1].set_ylabel("Время выполнения")
axs[1].plot(matrix_size, t1_det)
axs[1].plot(matrix_size, t_det)

axs[2].set_title("Транспонирование",fontsize = 12)
axs[2].set_xlabel("Размер матрицы")
axs[2].set_ylabel("Время выполнения")
axs[2].plot(matrix_size, t1_trans)
axs[2].plot(matrix_size, t_trans)

fig.legend(fontsize=8,
           ncol=1,
           edgecolor='b',
           title='Прямые',
           title_fontsize='15')
plt.subplots_adjust(wspace=.7, hspace=.7)
plt.show()