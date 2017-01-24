import re


def done_text(fname):
    f = open(fname, 'r', encoding='UTF-8')
    s = f.read().split()
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"1234567890«»”“><')
    f.close
    return s


def print_words(s):
    regex = '.*[ауоиыеюя].*[ауоиыеюя].*[ауоиыеюя].*'
    for word in s:
        if re.search(regex, word):
            print(word)


def main():
    textik = done_text(input('Введите имя файла с расширением: '))
    print_words(textik)


main()
    
