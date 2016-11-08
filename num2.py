names = ['Оля','Маша','Коля','Костя','Нина','Ира']
surnames=['Кузнецова', 'Сидорова', 'Семенов', 'Иванов', 'Илларионова']
if len(names) >= len(surnames):
    for i in range(len(surnames)):
        strng = names[i] + ' ' + surnames[i]
        print(strng)
    check = len(surnames)
    while check < len(names):
        print(names[check])
        check += 1
else:
    for i in range(len(names)):
        strng = names[i] + ' ' + surnames[i]
        print(strng)
    check = len(names)
    while check < len(surnames):
        print(surnames[check])
        check += 1
