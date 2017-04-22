import os


def count_dep():
    count = 0
    for root, dirs, files in os.walk('.', topdown=False):
        if len(root.split(os.sep)) - 1 > count:
            count = len(root.split(os.sep)) - 1
    with open('answer_sheet14.txt', 'w', encoding='UTF-8') as answer:
        answer.write(str(count))

def main():
    count_dep()


if __name__ == '__main__':
    main()