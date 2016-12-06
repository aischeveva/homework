f = open('freq_crlf.txt', 'r', encoding='utf-8')
s = f.read().split('\n')
f.close()
while True:
    word = input('Введите слово: ')
    if word == '':
        print('Завершение работы программы')
        break
    else:
        check = False
        for line in s:
            line = line.split(' | ')
            if word == line[0]:
                print(' | '.join(line))
                check = True
        if check is False:
            print('Такого слова в словаре нет.')
