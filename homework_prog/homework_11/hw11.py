import re


def change_text():
    f = open('mosq1.txt', 'r', encoding='UTF-8')
    s = f.read()
    f.close()
    s1 = re.sub('Комар(»| |а|ы|у|ом|е|ов|ам|ами|ах)', 'Слон\\1', s)
    s1 = re.sub('комар(»| |а|ы|у|ом|е|ов|ам|ами|ах)', 'слон\\1', s1)
    f = open('antwort.txt', 'w', encoding='UTF-8')
    f.write(s1)
    f.close()


def main():
    change_text()


if __name__ == '__main__':
    main()