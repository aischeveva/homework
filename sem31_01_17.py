import re


def find_space(fname):
    f = open(fname, 'r', encoding='UTF-8')
    s = f.read().split()
    regex = '«[a-zA-ZА-Яа-я]+?-[0-9]'
    wlist = re.findall(regex, s)
    print(', '.join(wlist))


def main():
    find_space('test.txt')


main()
