from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def vector_gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)  # concatenate заодно и скопирует
    d = len(ab)  # размер по старшему измерению

    # прямой
    for i in range(d):
      ab_ii = ab[i, i]
      ab[i] = ab[i]/ab_ii
      for j in range(i+1,d):
        ab[j] = ab[j] - ab[i] * (ab[j,i])


    # обратный
    for i in range(d - 1, -1, -1):
      for j in range(i - 1, -1, -1):
        ab[j] = ab[j] - ab[i] * (ab[j,i])


    x = ab[:, -1]  # Последний столбец
    return x

