# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(str(' '.join(str(val) for val in self.data[i])) for i in range(len(self.data)))

    def __add__(self, other):
        res_i = []
        res_j=[]
        sum_matrix = Matrix
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res_i.append(self.data[i][j] + other.data[i][j])
            res_j.append(res_i)
            res_i=[]
        return sum_matrix(res_j)

m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[10, 20], [30, 40], [50, 80]])
# print(m1)
print(m1 + m2)
