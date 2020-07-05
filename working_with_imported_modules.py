import time
import os
#working on windows using this to specify filepath
here = os.path.dirname(os.path.abspath(__file__))

while True:
    if os.path.exists("%s/files/vegetables.txt" % (here)):
        with open("%s/files/vegetables.txt" % (here)) as file:
            print(file.read())
    else:
        print("File does not eists.")
            
    time.sleep(10)
    break