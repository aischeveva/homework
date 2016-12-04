f = open('input.txt', 'r', encoding='UTF-8')
s = f.read().split('\n')
f.close()
avgsum = 0
for indx, line in enumerate(s):
    s[indx] = line.split()
    avgsum += len(s[indx])
print(u'Среднее количество слов в строке = {0}'.format(avgsum / len(s)))