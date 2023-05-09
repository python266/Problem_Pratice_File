from functools import lru_cache
FibArray = [0, 1]
@lru_cache(maxsize=10000000000000000)
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]
print(fibonacci(450))
