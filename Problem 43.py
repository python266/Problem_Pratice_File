x = [1, 2, 3, 4, 5, 5]
new = []
for i in x:
    count1 = x.count(i)
    if count1 > 1:
        new.append(i)

if len(new) == 0:
    print("Nothing is duplicate")
else:
    print("Yes something is duplicate")