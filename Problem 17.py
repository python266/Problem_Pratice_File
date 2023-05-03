def Palindromic_String():
    s = input("Enter the string: ")
    x = s[::-1]
    if x == s:
        print("YES")
    else:
        print("NO")
#driver code
if __name__ == '__main__':
    Palindromic_String()