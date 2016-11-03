import re
word = input("Введите слово на кириллице: ")
pattern1 = r'[А-Яа-я]'
pattern2 = r'[1-9A-Za-z]'
if re.match(pattern1, word) and re.search(pattern2, word) is None:
    for indx, letter in enumerate(word):
        if indx % 2 != 0:
            if letter != "а" and letter != "к":
                    print(letter)
else:
    print("Вводить можно только кириллицу :Р")