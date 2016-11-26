while True:
    s = input("Введите строку: ")
    if s == "":
        break
    for indx, part in enumerate(s):
        print(s[:len(s) - indx])