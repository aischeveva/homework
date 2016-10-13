my_num = 9
your_num = int(input('Write a number from 1 to 10, please: '))
if your_num == my_num:
    print('You\'re lucky one :D')
else:
    if your_num > my_num:
        print('Your number is too big')
    else:
        print('Your number is too small')
    your_num = int(input('Try again: '))
    if your_num == my_num:
        print('You\'re lucky one :D')
    else:
        print('You\'re hopeless')
