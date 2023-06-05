#Question 2
import json

a = {"Himesh": "Coder",
     "Car": [None],
     "Class": (9, "A"),
     "Sex": "Male"}

b = json.dumps(a)
print(b)

#Question 3
with open("Currency-conveter.json") as c:
    print(json.load(c))
c.close()

#Question 5
d= '{"name": "Bob", "languages": ["English", "French"], "Love with sister": "True"}'
e = json.loads(d)
print(e)

