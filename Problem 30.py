#Try, except and finally
#This is my own code
try:
    def divsion():
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        divsion_of_that_nums = a / b
        print(f"Your answer is {divsion_of_that_nums}.")
    divsion()
except:
    raise ZeroDivisionError("Sorry bro something went wrong")

#This code is made by Chat GPT.
def divsion():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    divsion_of_that_nums = a / b
    print(f"Your answer is {divsion_of_that_nums}.")

try:
    divsion()
except ZeroDivisionError:
    raise ZeroDivisionError("Sorry, division by zero is not allowed.")