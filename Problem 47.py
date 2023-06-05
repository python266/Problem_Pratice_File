import json

d = '{"var1":"harry", "var2":56}'

f = json.loads(d)

data2 = {"Name:": "Himesh Gupta",
         "Class:": (9, "A"),
         "Rich:": False}

secound = json.dumps(data2,indent=3,sort_keys=True)
print(secound)