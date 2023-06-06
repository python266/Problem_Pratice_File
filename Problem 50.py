input_user = input("-> ")
input_user_split = input_user.split(' ')
converting = [int(i) for i in input_user_split]
new_list = []
for items in converting:
    if items%2==0:
        new_list.append(items)
    elif items%2!=0:
        pass
print(new_list)
sum_of_newlist = sum(new_list)
print("The sum of the list is ",sum_of_newlist)