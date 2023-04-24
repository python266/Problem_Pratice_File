#2+4 = 6
#6+2 = 8

prev= 0
def SumOfPreviousNumber():
    global prev
    for i in range(10+1):
        x = prev + i
        print(x)
        prev = i
SumOfPreviousNumber()

