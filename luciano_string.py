# Leia strings do teclado até que uma string vazia seja lida. Escreva no vídeo:
# (a) a quantidade de vogais lidas;
# (b) a quantidade de dígitos lidos;
# (c) qual foi a string de maior comprimento lida. Caso haja empate, escreva uma delas;

while True:
    mystr = input("Entre com string:>> ")
    if not mystr: break
    vogais = [*map(mystr.lower().count, "aeiou")]
    digitos = len(mystr)
    print("{} vogais (a:{}, e:{}, i:{}, o:{}, u:{}), {} caracteres.".format(sum(vogais), *vogais, digitos))

