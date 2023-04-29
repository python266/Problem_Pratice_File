name = input("Enter your name--> ")
if name.isdigit():
    raise Exception("Sorry!Something went wrong!")
else:
    print(f"Welcome! {name} to our program")
def Leapyear():
    year = int(input("\nEnter the year: "))
    if year%400!=0:
        print(f"No! {year} is not leap year")
    elif year%400 == 0:
        print(f"Yes! {year} is a leap year")
Leapyear()