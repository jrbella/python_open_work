#Quick little script for fun

def ninety_nine_bottles_of_beer():
    bottles = 99
    word = "bottles"



    while bottles > 0:
        #Changing the plural
        if bottles == 1:
            word = "bottle"

        print(f"""  %s %s of beer on the wall, 
        %s %s of beer, you take one down, 
        you pass it around. %s %s of beer on the wall""" % (bottles,word, bottles, word, (bottles - 1), word))
        bottles -= 1
        
ninety_nine_bottles_of_beer()