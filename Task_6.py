# def det2(matrix):
#     return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#
#
# def minor(matrix, i, j):
#     tmp = [row for k, row in enumerate(matrix) if k != i]
#     tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
#     return tmp
#
#
# def det(matrix,a=None,b=None):
#     size = len(matrix)
#     if size == 2:
#         return det2(matrix)
#
#     return sum((-1) ** j * matrix[0][j] * det(minor(matrix, 0, j))
#                for j in range(size))

def matrix_inp(i):
    while True:
        try:
            line = list(map(int, input(f"Введите {i + 1} строку через пробел: ").split()))
            break
        except ValueError:
            print("Неверный ввод")
    if len(line) == columns:
        return line
    else:
        print("Неверно введены данные")
        return matrix_inp(i)

def matrix_outp(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()

def det(array,raws,columns):
    if raws == columns:
        if len(array) == 2:
            return array[0][0] * array[1][1] - array[0][1] * array[1][0]
        else:
            sum = 0
            for i in range(len(array)):
                new_array = []
                for j in range(1, len(array)):
                    line = []
                    for k in range(len(array[j])):
                        if k != i:
                            line.append(array[j][k])
                    new_array.append(line)
                sum += array[0][i] * (-1) ** ((i + 1) + (0 + 1)) * det(new_array,raws,columns)
        return sum
    else:
        print("Определитель найти невозможно")

def transpon(array,raws,columns):
    transpon_array = []
    for i in range(columns):
        line = []
        for j in range(raws):
            line.append(0)
        transpon_array.append(line)
    for i in range(len(array)):
        for j in range(len(array[i])):
            transpon_array[j][i] = array[i][j]
    # print("Транспонированная матрица :")
    # for i in range(len(transpon_array)):
    #     for j in range(len(transpon_array[i])):
    #         print(transpon_array[i][j], end=" ")
    #     print()

def squared(array,raws,columns):
    if raws == columns:
        square_array = []
        for i in range(len(array)):
            line = []
            for j in range(len(array[i])):
                line.append(0)
            square_array.append(line)
        for i in range(len(array)):
            for j in range(len(array[i])):
                for z in range(len(array)):
                    square_array[i][j] += array[i][z] * array[z][j]
        # print("Квадрат матрицы :")
        # matrix_outp(square_array)
    else:
        print("Количество строк не совпадает с количеством столбцов")


# columns = int(input(f"Введите кол-во столбцов матрицы "))
# raws = int(input(f"Введите кол-во строк матрицы "))
# a = []
# for i in range(columns):
#     a.append(matrix_inp(i))
# matrix_outp(a)
# print(det(a))
# print(squared(a))



def det(array, lines, columns):
    if lines == columns:
        if len(array) == 2:
            return array[0][0] * array[1][1] - array[0][1] * array[1][0]
        else:
            sum = 0
            for i in range(len(array)):
                new_array = []
                for j in range(1, len(array)):
                    line = []
                    for k in range(len(array[j])):
                        if k != i:
                            line.append(array[j][k])
                    new_array.append(line)
                sum += array[0][i] * (-1) ** ((i + 1) + (0 + 1)) * det(new_array, lines - 1, columns - 1)
        return sum
    else:
        print("Определитель найти невозможно")
