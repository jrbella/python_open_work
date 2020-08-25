#Quick little script for fun

def ninety_nine_bottles_of_beer():
    bottles = 99
    while bottles > 1:
        print(f"""  %s bottles of beer on the wall, 
        %s bottles of beer, you take one down, 
        you pass it around. %s bottles of beer on the wall""" % (bottles, bottles, (bottles - 1)))
        bottles -= 1
        
ninety_nine_bottles_of_beer()