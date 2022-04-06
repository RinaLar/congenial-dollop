cpdef test(int n):
    if n in (1, 2):
        return 1
    return test(n - 1) + test(n - 2)