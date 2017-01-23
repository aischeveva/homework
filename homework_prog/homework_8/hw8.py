import random


def ask_name():
    return input('Введите имя файла с расширением: ')


def get_words():
    f = open(ask_name(), 'r', encoding='UTF-8')
    s = f.read().split('\n')
    f.close()
    dic = {}
    for ln in s:
        temp = ln.split(',')
        dic[temp[0]] = temp[1:]
    return dic


def guess_word(word):
    num = len(word)
    if num <= 4:
        print('У вас {0} попытки'.format(num))
    else:
        print('У вас {0} попыток'.format(num))
    while num > 0:
        temp = input('Введите слово: ')
        if temp == word:
            print('Вы угадали!')
            break
        else:
            print('Попробуйте еще раз!')
            num -= 1
    if num == 0:
        print('Повезет в другой раз!')


def game(d):
    num_check = 0
    for k in d:
        print('Подсказка! {0} ...'.format(random.choice(d[k])))
        guess_word(k)
        num_check += 1
        if num_check == len(d):
            print('Это было последнее слово. Приходите еще')
            break
        ask = input('Хотите попробовать еще раз? Введите только "да" или "нет": ')
        if ask == 'нет':
            break

def main():
    d = get_words()
    game(d)


main()