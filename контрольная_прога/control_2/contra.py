import re


def open_file():
    f = open('islandic.xml', 'r', encoding='UTF-8')
    s = f.read()
    f.close()
    return s


def count_lines():
    s = open_file()
    s = s.split('\n')
    f = open('answer_length.txt', 'w', encoding='UTF-8')
    f.write(str(len(s)))
    f.close()

def my_diction(arr):
    dix = {}
    for word in arr:
        if word in dix:
            dix[word] += 1
        else:
            dix[word] = 1
    return dix


def create_diction():
    s = open_file()
    regex = '<w lemma=\".+?\" type=\"(.+?)">'
    arr = re.findall(regex, s)
    dix = my_diction(arr)
    f = open('answer_keys.txt', 'w', encoding='UTF-8')
    f.write('Отсортированный список морфологических разборов:\n')
    for key in sorted(dix):
        f.write(key + '\n')
    f.close()


def count_adj():
    s = open_file()
    regex = '<w lemma=\".+?\" type=\"(l.f.+?)">'
    arr = re.findall(regex, s)
    dix = my_diction(arr)
    f = open('answer_adj.txt', 'w', encoding='UTF-8')
    for key in sorted(dix):
        f.write(key + ' ' + str(dix[key]) + '\n')
    f.close()


def create_csv():
    s = open_file()
    print(s)
    regex1 = '<w lemma=\"(.+?)\" type=\"(.+?)\">(.+?)</w>'
    regex2 = '<.+?>\n'
    s = re.sub(regex1, '\\1, \\2, \\3', s)
    s = re.sub(regex2, '', s)
    s = re.sub('( )+?', '', s)
    s = s.split('\n')
    f = open('answer_dict.csv', 'w', encoding='UTF-8')
    for line in s:
        f.write(line + '\n')
    f.close()


def main():
    count_lines()
    create_diction()
    count_adj()
    create_csv()


if __name__ == '__main__':
    main()
