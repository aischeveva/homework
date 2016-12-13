def doneText(fname):
    f = open(fname, 'r')
    s = f.read().split(' ')
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"')
    f.close
    return s
fnm = input('Введите имя файла: ')
arr = doneText(fnm)
print('Количество слов в тексте = {0}'.format(arr.len()))
