from functools import lru_cache


@lru_cache(maxsize=100000)
def square_list():
    print("Enter the number just like this: 3, 3, 4")
    #ip = [2, 3, 3, 4, 5]
    ip = input("Enter the number: ")
    sp = ip.split(",")
    x = [int(j) for j in sp]
    for intem in x:
        s = pow(intem, 2)
        print("Square number of you list is;")
        print(s)
if __name__ == '__main__':
    square_list()
