def done_text(fname):
    f = open(fname, 'r')
    s = f.read().split()
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"1234567890«»><')
    f.close
    return s


def get_fname():
    return input("Введите имя файла с расширением: ")


def count_ing(arr):
    res = 0
    for word in arr:
        if word.endswith('ing'):
            res += 1
    return res


def count_form(arr, form):
    res = 0
    for word in arr:
        if word == form:
            res += 1
    return res


def main():
    textik = done_text(get_fname())
    print('Всего в тексте {0} форм на -ing'.format(count_ing(textik)))
    form = input('Введите форму, количество вхождений которой хотите найти: ')
    print('Эта форма встречается {0} раз'.format(count_form(textik, form)))


main()