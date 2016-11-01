my_num = 9
check = False
your_num = int(input('Write a number from 1 to 10, please: '))
while(your_num != my_num):
    if your_num > my_num:
        print('Your number is too big')
    else:
        print('Your number is too small')
    try:
        your_num = int(input('Try again: '))
    except ValueError:
        print("Not a number")
        check = True
        break
if check == True:
    print("See you next time")
else:
    print("You're right")
