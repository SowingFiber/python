import json
from difflib import get_close_matches

data = json.load(open('dictionary.json'))


def dictionary(w):
    w = w.upper()
    response = 'N'
    c_m = get_close_matches(w, data.keys())
    if w in data:
        print(data[w])
    elif len(c_m) > 0:
        response = input(
            'Did you mean ' + c_m[0] + ' or ' + c_m[1] + ' or ' + c_m[2] + '?\nPress (y) or (n): ')
        response = response.strip()
        if response == 'y' or response == 'Y':
            num_response = input(
                'So which is it?' + '\n1: ' + c_m[0] + '\n2: ' + c_m[1] + '\n3: ' + c_m[2] + '\n')
            print(data[c_m[int(num_response)-1]])
        else:
            print('Sorry, I have some difficulty understanding you, T.T')
    else:
        print('Sorry,', w, 'is not included in this dictionary! \ (* ^ *\')/')


word = input('Enter a word: ')
dictionary(word)
