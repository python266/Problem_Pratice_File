from functools import lru_cache


@lru_cache(maxsize=1000000000)
def large_product():
    a = input("Enter the num a: ")
    b = input("Enter the num b: ")
    if int(a) == 0:
        print(0)
    else:
        product = int(a) * int(b)
        print(product)

if __name__ == '__main__':
    large_product()
