#import
import os

here = os.path.dirname(os.path.abspath(__file__))

""" Old Code
myfile = open("%s\\fruit.txt" % (here))
content = myfile.read()
myfile.close()
"""

#adding with context manager
with open("%s\\fruit.txt" % (here)) as myfile:
    content = myfile.read()

print(content)

#retrieving from file directory
with open("%s/files/fruit_2.txt" % (here)) as myfile:
    content_2 = myfile.read()

print(content_2)

#writing data to file
#could add user input to add vegatables to file later use input etc
with open("%s/files/vegatables.txt" % (here), "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")

#retrieving vegatables
with open("%s/files/vegatables.txt" % (here)) as myfile:
    content_3 = myfile.read()

print(content_3)

#appending
#using the '+' to read the file and a .seek(0) method to move the 
#cursor back to the first indicie of the file
with open("%s/files/fruits.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()