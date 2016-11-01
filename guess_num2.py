my_num = 9
check = False
while (check == False):
    try:
        your_num = int(input('Write a number from 1 to 10, please: '))
    except ValueError:
        print("It's not a number, I'm out")
        break
    if your_num == my_num:
        print('You\'re lucky one :D')
        check = True
    else:
        if your_num > my_num:
            print('Your number is too big')
        else:
            print('Your number is too small')

print("End of programme")
