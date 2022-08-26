
mast_pwd = input('Please enter the master password? ')

def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")



while True:
    mode = input('Would you like to add a password or view your passwords? (view, add)?\n or press "q" to quit ')
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode. Please try again.')
        continue
