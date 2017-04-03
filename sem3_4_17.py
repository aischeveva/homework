def done_text():
    f = open('ostin.txt', 'r', encoding='utf-8')
    s = f.read().lower().split()
    f.close()
    for indx, word in enumerate(s):
        s[indx] = word.strip('.,:;№-*!?/|\[]{}()\'"1234567890«»><')
    return s


def count_words(arr):
    d = {}
    for word in arr:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def count_letters(arr):
    dic = {}
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for letter in alpha:
        dic[letter] = 0
    for word in arr:
        if word and word[0] in dic:
            dic[word[0]] += 1
    return dic

def count_pos(arr):
    dic = {key:ind for ind, key in enumerate(arr)}
    return dic

    
def create_antw(dic):
    f = open('answer_keys2.tsv', 'w', encoding='UTF-8')
    for key in sorted(dic):
        f.write('{0}\t{1}\n'.format(key, str(dic[key])))
    f.close()


def main():
    textik = done_text()
    create_antw(count_pos(textik))


if __name__ == '__main__':
    main()
