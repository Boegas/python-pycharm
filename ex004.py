a = input('\033[mDigite algo: ')
print('\033[1;31;43mO tipo primitivo desse valor é ', type(a))
print('\033[4;35;41mSó tem espaços? ', a.isspace())
print('\033[32;44mÉ um número? ', a.isnumeric())
print('\033[7;36;47mÉ alfabetico? ', a.isalpha())
print('\033[1;33;44mEsta em maiuscula? ', a.isupper())
print('\033[31;41mEsta em minuscula? ', a.islower())
print('\033[7;36;42mEsta capitalizada? ', a.istitle()) #maiuscula junto com minuscula