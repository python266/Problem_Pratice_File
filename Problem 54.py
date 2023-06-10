from collections import Counter

user_input = input("Enter the string: ")

count_particular = input("Enter the words: ")

method = Counter(user_input)

count = method.get(count_particular, 0)
print(count)