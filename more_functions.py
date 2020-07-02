#imports

#basic function for area

def area(a, b):
    return a * b

print(area(4,5))

#explicit function argument

def area_2(a,b):
    try:
        if(isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return a * b
        else:
            return (float(a) * float(b))

    except ValueError:
        return "The first parameter: [%s] or the second parameter [%s] were not valid arguments please enter either a float or an int" % (a, b)


#quick test

print(area_2(4,5)) #should be 20 
print(area_2(4.1, 5.1)) #should be 20.909...
print(area_2("4.1", "5.1")) #shoudl be 20.909..
print(area_2("this should fail", "this should fail")) #should throw


#indefinate paramters

def average_basic(*args):
    return (sum(args)/len(args))


#quick test
print(average_basic(1,2,3,4,5,6,7))

#sorting strings alphabetically

def alphabetize_list(*args):
    #converting the tuple to a list for processing
    args = [i.upper() for i in args]
    return sorted(args)

#quick test

print(alphabetize_list("twinkle","twinkle","little", "star"))