address = ['Flat number 30', 'Sesame Street', 'Silicon Valley']
pins = {'Mike': 2121, 'James': 3243, 'Connor': 2312}
print(address[0], address[1])

pin = int(input('Enter your pin: '))


def find_the_fruit(f):
    myfile = open("files/sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return f + ' found in the dictionary...\nEnabling access...'
    else:
        return f + ' not found!\nRevoking access...'


if pin in pins.values():
    fruit = input('Enter a fruit: ')
    print(find_the_fruit(fruit))
else:
    print('Incorrect pin')
    print('This house can only be accessed by: ')
    for user in pins:
        print(user)
