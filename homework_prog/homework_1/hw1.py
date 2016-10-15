temp = False
while (temp == False):
    try:
        a = float(input('Введите первое число (a) '))
        b = float(input('Введите второе число (b) '))
        c = float(input('Введите третье число (c) '))
        temp = True
    except (TypeError, ValueError):
        print('Просила же только числа вводить!')
if a + b == c:
    print('Поздравляю! a + b = c')
else:
    print('Прошу прощения, но a + b != c')
if a*c + b == 0:
    print('Поздравляю! a*c + b = 0')
else:
    print('Прошу прощения, но a*c + b != 0')