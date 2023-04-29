def logic():
    n = int(input("Enter the number: "))
    if n%2 != 0:
        print('Weird')
        exit()
    lsi2 = [j for j in range(2,6)]
    if n in lsi2:
        print("Not Weird")
        exit()
    lsi = [x for x in range(6, 21)]
    if n in lsi:
        print("Weird")
        exit()
    if n > 20:
        print("Not Weird")
        exit()
logic()