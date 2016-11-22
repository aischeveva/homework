coinc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    s = input('Введите текст: ')
    if s == '':
        break
    s = s.split()
    res = ''
    if s[0] == 'decode':
        s.pop(0)
        s = ' '.join(s)
        for letter in s:
            if letter == '!':
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
    else:
        if s[0] == 'code':
            s.pop(0)
        s = ' '.join(s)
        for letter in s:
            if letter == ' ':
                res += '!'
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
