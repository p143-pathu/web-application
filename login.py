print('please enter your username')
username = input()
if username == 'Prathyusha' or username == 'Pathu':
    print('Hello again ' +username + 'please enter your password')
    password = input()
    if username == 'Sanjin' and password == 'Abc':
        print('ACCESS GRANTED')
    elif username == 'Bob' and password == 'Alpha':
        print('ACCESS GRANTED')
    else:
        print('Incorrect Password!')
        print('ACCESS DENIED')
else:
    print('No such username!')
    print('ACCESS DENIED')