#password generator
import random
import string

letters = string.ascii_letters
digit = string.digits
punctuation = string.punctuation

add_strings = letters + digit + punctuation

new_pass = ""
len_pass = 3

password = random.choices(add_strings, k=len_pass)

for i in password:
    print(i, end='')