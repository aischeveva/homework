word = input('Write a word in cyrillic: ')
if word.endswith('о'):
    print('Possible forms: Nom. Sg. / Acc. Sg.')
elif word.endswith('а'):
    print('Possible forms: Gen. Sg. / Nom. Pl. / Acc. Pl.')
elif word.endswith('у'):
    print('Possible forms: Dat. Sg.')
elif word.endswith('ом'):
    print('Possible forms: Instrum. Sg.')
elif word.endswith('е'):
    print('Possible forms: Prep. Sg.')
elif word.endswith('ам'):
    print('Possible forms: Dat. Pl.')
elif word.endswith('ами'):
    print('Possible forms: Instrum. Pl.')
elif word.endswith('ах'):
    print('Possible forms: Prep. Pl.')
else:
    print('Possible forms: Gen. Pl.')
