import re


def ask_name():
    return input('Введите имя файла с расширением: ')


def get_words():
    f = open(ask_name(), 'r', encoding='UTF-8')
    s = f.read().split()
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"1234567890«»><')
    f.close
    return s


def count_words(words):
    regex = 'откр(ы|о)((т(ый|ая|ое|ые|ого|ой|ых|ому|ым|ую|ом|ою)|в(ш(ий?|ая|ее|ие|его|ей|их|ему|им|ую|ею))?)|(л(а|о|и)?)|(й(те)?)|(ют?|е(шь|м|те?)))(ся|сь)?'
    wlist = []
    for word in words:
        if re.fullmatch(regex, word):
            if word not in wlist:
                wlist.append(word)
    return wlist


def main():
    print(', '.join(count_words(get_words())))


main()