import os
import re
import math
from math import log

PUNCT = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'


def preprocessing(text): # функция предобработки текста
    text_wo_punct = re.sub(PUNCT, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    words = text_wo_punct.strip().split() # делим по пробелам
    return words


def count_tf(word, text): # считаем, сколько раз слово встретилось в тексте и делим на общее количество слов (как в pmi)
    return text.count(word) / len(text)


def count_df(word, texts): # считаем, в скольких текстах встретилось слово
    n = [1 for text in texts if word in text]
    return sum(n)


def count_idf(word, texts):
    n = len(texts) / (1 + count_df(word, texts))
    return n


def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    return log(tf, 10) * log(idf, 10)


def get_texts():
    texts_dic = {}
    for root, dirs, files in os.walk('wikipedia'):
        for f in files[:50]:
            with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
                text = preprocessing(t.read())
                texts_dic[f.split('.')[0]] = text
    texts = list(texts_dic.values())
    return texts_dic, texts


def fin_output(texts_dic, texts):
    for text in texts_dic:
        print("Top words in document {}".format(text)) # чтобы было понятно, какой документ мы обрабатывали
        scores = {} # здесь будем хранить оценки для каждого текста
        for word in texts_dic[text]:
            scores[word] =  count_tfidf(word, texts_dic[text], texts)
        sorted_words = sorted(scores.items(), key=lambda x: x[1])
        for word, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


def main():
    a = get_texts()
    fin_output(a[0], a[1])


if __name__ == '__main__':
    main()
