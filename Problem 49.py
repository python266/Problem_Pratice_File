i = input("Enter the nums: ")
split_i = i.split(' ')
converting = [int(k) for k in split_i]

largest = 0
second_largest = 0
for j in converting:
    if j > largest:
        largest = second_largest
        second_largest = j
    elif j > second_largest:
        second_largest = j
print(second_largest)