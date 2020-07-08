import os
import json
from difflib import get_close_matches

here = os.path.dirname(os.path.abspath(__file__))

data_file = "%s/data.json" % (here)

data = json.load(open(data_file))

def translate(w):
    #user input cleanup
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word [%s] doesn't exist. Please double check it." % (word)
        else:
            return "We didn't understand your query"
    else:
        return "The word [%s] doesn't exist. Please double check it." % (word)

word = input("Enter word: ")

output = (translate(word))

#testing
#print(translate(word))

#will handle list items
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)