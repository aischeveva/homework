def done_text(fname):
    f = open(fname, 'r')
    s = f.read().split()
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"1234567890«»><')
    f.close
    return s


def count_syll(arr, n):
    res = []
    voc = 'аоуыиеёюя'
    for word in arr:
        num = 0
        for letter in word:
            if letter in voc:
                num += 1
        if num == n:
            res.append(word)
    return res

def first_letter(arr, letter):
    res = []
    for word in arr:
        if word.startswith(letter):
            res.append(word)
    return res

def choice():
    fnm = input('Введите имя файла: ')
    textik = done_text(fnm)
    make_choice = input('Если хотите, чтобы программа считала слоги, введите syllables; иначе - letter: ')
    if make_choice == 'syllables':
        numb = int(input('Введите количество слогов в словах: '))
        print(' '.join(count_syll(textik, numb)))
    else:
        lett = input('Введите желаемую первую букву: ')
        print(' '.join(first_letter(textik, lett)))

    
def main():
    choice()


main()
