s = input("Введите строку: ")
for indx, part in enumerate(s):
    print(s[:len(s) - indx])