from functools import lru_cache


@lru_cache(maxsize=1000000)
def natural(n):
    if n == 1:
        return 1
    else:
        return n + natural(n - 1)

print(natural(490))
