def done_text(fname):
    f = open(fname, 'r')
    s = f.read().split()
    for indx, word in enumerate(s):
        s[indx] = word.lower().strip('.,:;№-*!?/|\[]{}()\'"1234567890«»”“><')
    f.close
    return s


def freq_dic(arr):
    dic = {}
    for word in arr:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    return dic


def print_dic(dic):
    for word in dic:
        if dic[word] >= 10:
            print(word, dic[word])


def main():
    my_text = done_text(input('Введите имя файла с расшриением: '))
    print_dic(freq_dic(my_text))


main()
