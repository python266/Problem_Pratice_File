#DDXDDD-DD
inp = input("Enter Licence Plate Number: ")

def function():
    x = int(inp[0]) + int(inp[1]) + int(inp[3]) + int(inp[4]) + int(inp[5]) + int(inp[7]) + int(inp[8])

    list1 = ["A", "E", "I", "O", "Y"]
    if x%2==0 and inp[2] in list1:
        print("Yes This number is valid")
    else:
        print("No! This number isn't valid.")
if __name__ == '__main__':
    function()