#i.e
#x =[1, 3, 4, 5, 6]
#for i in x:
#    c = x[int(input("--> "))]
#    print(c)


#seven segment display
match_stick_no = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]

c = match_stick_no[int(input("Enter the equal to 9 or lower: "))]

if c <= 9:
    print(c)
elif c > 9:
    print("Out of range")