import re


def done_text(fname):
    f = open(fname, 'r', encoding='UTF-8')
    s = f.read().lower()
    rez1 = '(,|:|№|-|\*|/|\||\[|\]|{|}|\\|(|)|\'|"|[0-9]|«|»|>|<|V|I|X)+'
    s = re.sub(rez1, ' ', s)
    rez = '\.|\?|!|\.\.\.'
    s = re.split(rez, s)
    f.close()
    for indx, sent in enumerate(s):
        s[indx] = sent.split()
        if len(s[indx]) == 0:
            s.pop(indx)
    return s


def count_letters(arr):
    mlist = [(indx + 1, word, len(word)) for indx, senten in enumerate(arr) for word in senten if len(word) >= 7]
    f = open('answer_sheet12.txt', 'w', encoding='UTF-8')
    for k in mlist:
        f.write('предложение {0}, {1}-------{2}\n'.format(k[0], k[1], k[2]))
    f.close()


def main():
    count_letters(done_text('tolstoy.txt'))


if __name__ == '__main__':
    main()