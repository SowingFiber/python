correct_password = 'python123'
password = input('Enter the password: ')
attempts = 3
while password != correct_password and attempts > 1:
    attempts -= 1
    password = input('Wrong Password!\n' + str(attempts) +
                     " Attempts left\n" + 'Enter the password: ')
if attempts == 1:
    print('Not cool bro...')
if attempts > 1 and password == correct_password:
    print('Oh you got in?')
