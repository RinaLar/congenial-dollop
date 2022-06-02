from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

def vector_gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)  # concatenate заодно и скопирует
    d = len(ab)  # размер по старшему измерению

    # прямой
    for i in range(d):
      ab_ii = ab[i, i]
      ab[i] = ab[i]/ab_ii
      for j in range(i+1,d):
        ab[j] = ab[j] - ab[i] * (ab[j,i])
    # запрограмируйте!

    # обратный
    for i in range(d - 1, -1, -1):
      for j in range(i - 1, -1, -1):
        ab[j] = ab[j] - ab[i] * (ab[j,i])
    # запрограмируйте!

    x = ab[:, -1]  # Последний столбец
    return x



solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
