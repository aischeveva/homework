import os


def mk_ppk(s):
    s = s.split()
    pth = '.'
    for word in s:
        pth += os.sep + word
    if not os.path.exists(pth):
        os.makedirs(pth)    


def mk_fls(num):
    pth = '.'
    for ppk in range(num):
        pth += os.sep + str(ppk+1)
        if not os.path.exists(pth):
            os.makedirs(pth)
            for pp_quant in range(ppk+1):
                f = open(pth + os.sep + str(pp_quant + 1) + '.txt', 'w')
                f.close()
        pth = '.'
            
def prnt_dir(nm_dir):
    for fl in os.listdir(nm_dir):
        if os.path.isdir(fl):
            print(fl)


def main():
    mk_ppk(input('Введите приложение: '))
    mk_fls(int(input('Введите число: ')))
    prnt_dir('.')


if __name__ == '__main__':
    main()
