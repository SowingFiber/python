import random
import string

letters = string.ascii_lowercase

def randomString(length = 10):
    return ''.join(random.choice(letters) for i in range(length))
myString = randomString(int(random.randrange(32)))
print(myString)
print(len(myString))
print(randomString(32))