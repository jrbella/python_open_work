#import
import os

here = os.path.dirname(os.path.abspath(__file__))
myfile = open("%s\\fruit.txt" % (here))
content = myfile.read()
myfile.close()

print(content)