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
                        if i == 'Z':
                            res += 'A'
                        elif i == 'z':
                            res += 'a'
                        elif i == 'Я':
                            res += 'А'
                        elif i == 'я':
                            res += 'а'
                        else:
                            res += coinc[indx + 1]
        print (res)
print('Программа завершила свою работу!')        
