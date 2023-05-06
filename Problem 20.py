#Ai method
list_is = [23, 42, 24, 1000, 34]
max_num = -float('inf')
for i in list_is:
    if i > max_num:
        max_num = i
print(f"Maximum number is: {max_num}")

#own method
mylist = [45,3,5]
updatinglist = [10]

for i in range(len(mylist)):
    if updatinglist < mylist:
        updatinglist[0] = max(mylist)
        print(f"1The largest number in the list is {updatinglist}")
        break
    else:
        print("Sorry! something went wrong!")