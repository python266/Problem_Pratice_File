array1 = input("Enter the nums: ")

x = array1.split(' ')
s = [int(j) for j in x]

if s.pop()%10==0:
    print("Yes")
else:
    print("No")