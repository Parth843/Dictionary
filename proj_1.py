# An interactive dictionary

import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def get_meaning(w):
    w = w.lower()
    if w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),n = 3,cutoff = 0.6)) > 0:
        suggest = get_close_matches(w,data.keys(),n = 3,cutoff = 0.6)[0]
        response = input("Did you mean {}? press y or n: ".format(suggest))
        if response == 'y':
            return data[suggest]
        elif response == 'n':
            return 'The word does not exist !'
        else:
            return 'We did not understand your entry !'
    else:
        return 'The word was not found !'

word = input('Enter a word: ')

meaning = get_meaning(word)

if isinstance(meaning,list):
    for i in meaning:
        print('>>> ' + i)
else:
    print(meaning)