import work
import time


start_cy = time.time()
work.test(30)
end_cy = time.time()
cy_time = end_cy - start_cy

print(f'Время выполнения Cython: {cy_time}')


def test(n):
    if n in (1, 2):
        return 1
    return test(n - 1) + test(n - 2)



start_py = time.time()
test(30)
end_py = time.time()
py_time = end_py - start_py

print(f'Время выполнения Python {py_time}')