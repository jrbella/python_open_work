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