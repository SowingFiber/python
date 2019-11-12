users = ['mike', 'john', 'damien', 'khora']
userpass = [1234, 4231, 1111, 2222]

data = open('users.txt', 'w')
for i in range(len(users)):
    dataString = users[i] + ':' + str(userpass[i]) + '\n'
    data.write(dataString)
print('done')
data.close()
