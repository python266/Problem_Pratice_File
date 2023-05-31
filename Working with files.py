with open("Harryt.txt") as f:
    rlines = f.readlines()
em = {}
for lines in rlines:
    spl = lines.split("     ")
    em[spl[0]] = spl[1]
it = int(input("Enter the num: "))
x = [item for item in em.keys()]
g = input("Name: ")

print(it*float(em[g]))