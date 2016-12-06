f = open('freq_crlf.txt', 'r', encoding='utf-8')
s = f.read().split('\n')
f.close()
arr = []
while True:
    word = input('Введите слово: ')
    if word == '':
        print('Результаты:')
        break
    else:
        arr.append(word)
for word in arr:
    check = False
    for line in s:
        line = line.split(' | ')
        if word == line[0]:
            print(' | '.join(line))
            check = True
    if check is False:
        print(u'{0}: Такого слова в словаре нет.'.format(word))
print('Завершение работы программы')