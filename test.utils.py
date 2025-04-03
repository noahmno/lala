import math




def factorial(n):
    if n < 1:
        raise ValueError("plus petit que 0")
    return math.factorial(n)


print(factorial(0))