from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1 << 30)
@lru_cache
def Fibonacci(n):
    return Fibonacci(n - 1) + Fibonacci(n - 2) if n > 2 else 1 if n == 1 else 2
print(Fibonacci(int(input())))
