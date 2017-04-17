import os
import re


def rem_dir(name_dir):
    for root, dirs, files in os.walk('.', topdown=False):
        if re.findall(os.sep + name_dir, root):
            for f in files:
                os.remove(os.path.join(root, f))
            for d in dirs:
                os.rmdir(os.path.join(root, d))
        for d in dirs:
            if name_dir == d:
                os.rmdir(os.path.join(root, d))


def print_root():
    s = '--'
    for root, dirs, files in os.walk('.'):
        print (s + root)
        if len(dirs):
            s = '\t' + s
        for f in files:
            print('\t{0}'.format(f))

def main():
    rem_dir('wrong')
    print_root()


if __name__ == '__main__':
    main()
