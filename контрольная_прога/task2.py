import decimal
f = open('freq_crlf.txt', 'r', encoding='utf-8')
s = f.read().split('\n')
f.close()
ress = ''
ipm_sum = 0
for line in s:
    line = line.split(' | ')
    if line[1].find('ед жен') != -1:
        ress += line[0]
        ress += ', '
        ipm_sum += decimal.Decimal(line[2])
print(ress)
print(u'Суммарное значение ipm = {0}'.format(ipm_sum))