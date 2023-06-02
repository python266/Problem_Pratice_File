#vallid prantheses

x = ["()", "{}", "[]"]

user_inout = input("-> ")

correct = user_inout in x

if correct:
    print(True)
else:
    print(False)