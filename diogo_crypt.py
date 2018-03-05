import string
import random

abc = string.ascii_letters
bac = list(string.ascii_letters)
random.shuffle(bac)
bac = "".join(bac)
print("Chaves:")
print(abc)
print(bac)
my_key = dict(zip(abc,bac))
my_dekey = dict(zip(bac,abc))
print(my_key)

def crypt(strg,key):
    my_crypto = ""
    for letter in strg:
        my_crypto += key[letter]
    return my_crypto



putaria_secreta = crypt("Diogo", my_key)
print(putaria_secreta)

file = open('arquivo.txt', 'w')
file.write(putaria_secreta)
file.close()

file = open('arquivo.txt', 'r')
leitura_secreta = file.read()
file.close()


print(crypt(leitura_secreta,my_dekey))

