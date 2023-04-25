# Exercise 4: Remove first n characters from a string

st = "CCD Himesh"
print(st)

# remove CCD in given string
x= list(st.split(' '))
re = x.remove(x[0])
print(x)

# other i.e.
str1 = "Pyhacker"
#now We will remove hacker from the word
str1 = str1.replace(str1[2:],'')
print(str1)