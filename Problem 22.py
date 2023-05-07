ip = input("Enter the string: ")

new_str = ''

for i in ip:
    if i.isupper() == True:
        new_str += i.lower()
    elif i.islower() == True:
        new_str += i.upper()
print(new_str)