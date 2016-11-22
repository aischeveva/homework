check = True
while check is True:
    s = input("Введите текст: ")
    if s == "":
        check = False
    else:
        res = ""
        for letter in s:
            if ord(letter) == 90:
                res += chr(65)
            elif ord(letter) == 122:
                res += chr(97)
            elif ord(letter) == 1071:
                res += chr(1040)
            elif ord(letter) == 1103:
                res += chr(1072)
            else:
                res += chr(ord(letter) + 1)
        print (res)
print("Программа завершила работу")
