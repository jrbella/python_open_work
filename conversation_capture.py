#imports

#variables

interrogatives = ["Who", "What", "When", "Where", "Why", "How"]

def create_interrogative(interrogative):
    interrogatives.append(interrogative.title())
    return "Updated interrogatives with %s." % (interrogatives) 

def sentence_maker(phrase):
    capitilized = phrase.capitalize()
    #output for debugging
    #rint(phrase)
    for interrogative in interrogatives:
        if (capitilized.startswith(interrogative)):
            return "%s?" % (capitilized)
    return "%s." % (capitilized)

#Terminal Input for user
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
        
print(" ".join(results))