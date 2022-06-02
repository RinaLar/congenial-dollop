import Module_1

concatenate = Module_1.concatenate
array = Module_1.array


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
