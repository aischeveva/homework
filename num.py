words=[]
check = True
while check is True:
    inp = input("Введите слово: ")
    if inp == "":
        check = False
    else:
        words.append(inp)
for indx in range(len(words) - 1, -1, -1):
    print(words[indx])
