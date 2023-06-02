h = [1, 4, 5, 2, 7]

target = 3
found = False

for i in range(len(h)):
    for k in range(i+1, len(h)):
        if h[i] + h[k] == target:
            found = True
if found:
    print(True)
else:
    print(False)