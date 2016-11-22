check = True
coinc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while check is True:
    s = input('Введите текст: ')
    if s == '':
        check = False
    else:
        res = ''
        for letter in s:
            if letter == ' ':
                res += ' '
            else:
                for indx, i in enumerate(coinc):
                    if i == letter:
                        if i == 'A':
                            res += 'Z'
                        elif i == 'a':
                            res += 'z'
                        elif i == 'А':
                            res += 'Я'
                        elif i == 'а':
                            res += 'я'
                        else:
                            res += coinc[indx - 1]
        print (res)
print('Программа завершила свою работу!')   
