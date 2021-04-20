def fib(n):
    a = 0
    b = 1
    assert n >= 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


print(fib())
