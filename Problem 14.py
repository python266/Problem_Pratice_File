list1 = [23, 50, 89, 100]
list2 = [20,30,3494, 90]
list3 = []
print(list1)
print(list2)
for i in list1:
    if i%2==0:
        list3.append(i)
for j in list2:
    if j%3==0:
        list3.append(j)
else:
    print("\n")
    print(list3)