import os
import re


def count_dirs():
    res = '[0-9]'
    arr = [thing for thing in os.listdir('.') if os.path.isdir(thing) and len(re.findall(res, thing))]
    return arr


def print_answer(arr):
    fout = open('answer_sheet13.txt', 'w', encoding='UTF-8')
    fout.write('Всего папок с цифрами в названии - {0}.'.format(str(len(arr))))
    fout.write('Все имена в директории (без повторений):\n')
    clear_names = []
    for thing in os.listdir('.'):
        temp = thing
        if os.path.isfile(thing):
            temp = re.sub('\..+', '', thing)
        if temp not in clear_names:
            clear_names.append(temp)
    for nme in clear_names:
        if nme:
            fout.write(nme + '\n')
    fout.close()


def main():
    print_answer(count_dirs())


if __name__ == '__main__':
    main()