import os
import re


def count_words():
    with open('answer1.txt', 'w', encoding='utf-8') as fout:
        for root, dirs, files in os.walk('./news'):
            for f in files:
                count = 0
                with open(os.path.join(root, f), 'r') as fin:
                    f1 = fin.read().split()
                    for line in f1:
                        if '<w>' in line:
                            count += 1
                fout.write('%s \t %d \n' %(f, count))


def annot():
    with open('answer2.csv', 'w', encoding='utf-8') as fout:
        fout.write('Название файла \t Автор \t Дата создания')
        for root, dirs, files in os.walk('./news'):
            for f in files:
                with open(os.path.join(root, f), 'r') as fin:
                    f2 = fin.read()
                    nam = f
                    reg1 = '<meta content="(.+?)" name="author">'
                    reg2 = '<meta content="(.+?)" name="created">'
                    auth = re.search(reg1, f2).group(1)
                    date = re.search(reg2, f2).group(1)
                    fout.write('%s \t %s \t %s \n' %(f, auth, date))


def bigramms():
    with open('answer3.txt', 'w', encoding='utf-8') as fout:
        for root, dirs, files in os.walk('./news'):
            for f in files:
                with open(os.path.join(root, f), 'r') as fin:
                    f3 = fin.read().split('\n')
                    reg = '<w><ana .+?gr="(.+?)"></ana>(.+?)</w>'
                    for indx, sentence in enumerate(f3):
                        if '<w>' in sentence:
                            f3[indx] = [re.search(reg, sentence).group(1), re.search(reg, sentence).group(2)]
                        else:
                            f3.remove(sentence)
                    temp = True
                    for indx, word in enumerate(f3):
                        try:
                            if 'A' in word[0]:
                                if 'gen' in word[0]:
                                    if 'S' in f3[indx + 1][0]:
                                        if 'gen' in f3[indx + 1][0]:
                                            fout.write('%s %s \n' %(word[1], f3[indx + 1][1]))
                        except IndexError:
                            temp = False

def main():
    count_words()
    annot()
    bigramms()


if __name__ == '__main__':
    main()
