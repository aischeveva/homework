f = open('freq_crlf.txt', 'r', encoding='utf-8')
s = f.read().split('\n')
f.close()
for line in s:
    line = line.split(' | ')
    if line[1] == 'союз':
        print(' | '.join(line))
