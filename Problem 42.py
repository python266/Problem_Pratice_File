with open("Currency-conveter.txt") as f:
    x =f.readlines()
dict1 = {}
for lines in x:
    spl = lines.split("\t")
    dict1[spl[0]] = spl[1]
itinp = int(input("Enter the number: "))
[print(items) for items in dict1.keys()]
name = input("Enter the country: ")
print(f"{itinp} --> {itinp * float(dict1[name])}")