import json
import difflib

data = json.load(open("dataset.json"))
# print(type(data))

def translate(word):
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()] 
    elif word.capitalize() in data:
        return data[word.capitalize()]

    elif len(difflib.get_close_matches(word, data.keys()))>0:
            yn = input("Did you mean %s instead? [y]/n: " % difflib.get_close_matches(word, data.keys())[0])
            if (yn=="y"):
                return data[difflib.get_close_matches(word, data.keys())[0]]
            elif (yn=="n"):
                return "No such definition found in the dictionary."
            else:
                return "Sorry, inavlid input."
    else:
        return ("No definition found. Please double check the word.")

x = input("Enter word: \n")


output = translate(x.lower())

"""OUTPUT"""
#following conditions are there as translate function can return either a list or a string
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
