#try except bolck
#This is mine code:

#class FileFoundError(Exception):
#    pass

try:
    open("nonefile.txt", "r")
    print("Yes this file is exist.")
except:
    raise FileNotFoundError("Sorry Your file isn't exist")