#You can modify this code
def fun():
    i = int(input("Enter the number: "))
    max_num = 42
    if i <= max_num:
        return fun()
    elif i >= max_num:
        quit()
if __name__ == '__main__':
    fun()