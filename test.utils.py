import math




def test_factorial(n):
    if n < 1:
        raise ValueError("plus petit que 1")
    return math.factorial(n)


print(test_factorial(0))