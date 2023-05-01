#Write a Program to extract each digit from an integer in the reverse order.
i = int(input("Enter then number: "))

x = str(i)[::-1]
c = x.replace('', ' ')
print(c)
