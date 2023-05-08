class NumberLimitExceededException(Exception):
    pass
def count_divisors():
    print("Attention! Your number must be 3")
    ip = input("\nEnter the number with space: ")
    sp = ip.split(' ')
    ls = [int(x) for x in sp]
    if len(ls) > 3:
        raise NumberLimitExceededException("\t\tSorry! You have entered more than 3 numbers.Please try again.")
    else:
        ch = ls[0] + ls[1]
        if ch%ls.pop() == 0:
            print("Yes it has divisible by the last number.")
        else:
            print("Nope It has not divisible by the last number")
if __name__ == '__main__':
    count_divisors()