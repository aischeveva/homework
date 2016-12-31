import random


def generate_adj():
    f = open('adj.txt', 'r')
    s = f.read().split()
    f.close()
    return random.choice(s)


def generate_noun(num):
    if num == 'sg':
        f_name = 'noun_sg.txt'
    else:
        f_name = 'noun_pl.txt'
    f = open(f_name, 'r')
    s = f.read().split()
    f.close()
    return random.choice(s)


def generate_verb():
    f = open('verbs.txt', 'r')
    s = f.read().split()
    f.close()
    return random.choice(s)


def generate_punct(pos):
    if pos == 'end':
        f_name = 'end_punct.txt'
    else:
        f_name = 'mid_punct.txt'
    f = open(f_name, 'r')
    s = f.read().split()
    f.close()
    punct = random.choice(s)
    if punct == '-':
        punct = ' ' + punct
    return punct


def generate_pronoun():
    f = open('pronouns.txt', 'r')
    s = f.read().split()
    f.close()
    return random.choice(s)


def generate_intj():
    f = open('intj.txt', 'r')
    s = f.read().split('\n')
    f.close()
    return random.choice(s)


def generate_line(num):
    if num == 1:
        return generate_adj() + ' ' + generate_noun('sg') + generate_punct('end') + '\n'
    elif num == 2:
        return generate_verb() + ' ' + generate_noun('pl') + ' и' + '\n'
    else:
        return generate_pronoun() + generate_punct('mid') + ' ' + generate_intj() + generate_punct('end') + '\n'


def generate_haiku():
    return generate_line(1) + generate_line(2) + generate_line(3)


print(generate_haiku())