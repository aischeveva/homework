check = True
words = []
while check is True:
    s = input("Введите слово: ")
    if s == "":
        check = False
    else:
        temp = []
        for letter in s:
            temp.append(letter)
        words.append(temp)
for wrd in words:
    for letterindx in range(2, len(wrd), 2):
        if letterindx >= len(wrd):
            break
        wrd.pop(letterindx)
    s = ""
    for letterindx in range(len(wrd) - 1, -1, -1):
        s += wrd[letterindx]
    print(s)