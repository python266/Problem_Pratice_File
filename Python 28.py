import numpy
from functools import lru_cache
@lru_cache(maxsize=9000000)
def fun():
    int(input("Enter the length of the string: "))
    main_no = input("Enter the number: ")
    split = main_no.split(' ')
    x = [int(j) for j in split]
    ans = 1
    muliply_with_modules = (numpy.prod(x)) % (pow(10,9)+7)
    print(muliply_with_modules)
if __name__ == '__main__':
    fun()