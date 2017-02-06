import re


def search_inf(fname):
    f = open(fname, 'r', encoding='UTF-8')
    s = f.read()
    f.close()
    regex = '>Столица.*?([А-Яа-я]+(-[А-Яа-я]+)*)'
    res = re.search(regex, s, re.DOTALL)
    if res:
        k = open('answer.txt', 'w', encoding='UTF-8')
        print(res.group(1))
        k.write(res.group(1))
        k.close()


def main():
    search_inf(input('Введите имя файла: '))


if __name__ == '__main__':
    main()