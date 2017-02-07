import re


def split_txt():
    f = open('test1.txt', 'r', encoding='UTF-8')
    s = f.read()
    s.replace('\n', ' ')
    s1 = re.sub('(\?|!|\.\.\.|([а-яa-z.]+ [а-яa-zА-ЯA-Z]{2,}\.))', '\\1^', s)
    print(s1)


def main():
    split_txt()


main()
