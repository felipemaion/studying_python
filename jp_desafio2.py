
# Desafio 2:
# Escreva uma função que recebe uma string e uma lista de palavras proibidas e substitui a palavra proibida por *


import re # Usar Regular Expressions para ignorar Maiúsculas e afins...

def censurar(texto, *palavras):
    for palavra in palavras:
        texto = re.sub(palavra, str(palavra[0]) + "*"*(len(palavra)-1), texto, flags=re.IGNORECASE)
    return texto

def censurar1(texto, *palavras):
    for palavra in palavras:
        if palavra.upper() in texto.upper():
            texto = texto.upper().replace(palavra.upper(), "*"*len(palavra))
    return texto

def censurar2(texto, *palavras):
    for palavra in palavras:
        if palavra.upper() in texto.upper():
            texto = texto.replace(palavra, "*"*len(palavra))
    return texto


texto = "Texto sujo, para mostrar que quero que se foda! Se fOdA! Vai tomar no cu! Porra!"
palavras = ["cu", "foda", "porra", "puta", "caralho", "desgraça", "arrombado", "desgraca", "fdp"]
print("Texto original:", texto)
print("Palavras a serem censuradas:", palavras)
print("\nMétodo com Regular Expression:")
print(censurar(texto, *palavras))
print("\nMétodo com String - Mudando para Upper case:")
print(censurar1(texto,*palavras))
print("\nMétodo com String - Sem mudar para Upper case:")
print(censurar2(texto,*palavras))
#
# def interface():
#     print("="*38)
#     print("Olá, bem vindo")
#     print("="*38)
# interface()
# def text():
#     texto = input("->").upper()
#     return texto
# # texto = text()
# def white_list(texto):
#     if "PORRA" in texto:
#         texto = texto.replace("PORRA", "Po***")
#     if "PUTA" in texto:
#         texto = texto.replace("PUTA", "P***")
#     if "CARALHO" in texto:
#         texto = texto.replace("CARALHO", "Ca*****")
#     if "DESGRAÇA" in texto:
#         texto = texto.replace("DESGRAÇA", "De******")
#     if "CU" in texto:
#         texto = texto.replace("CU", "C*")
#     if "ARROMBADO" in texto:
#         texto = texto.replace("ARROMBADO", "A********")
#     texto = texto.capitalize()
#     print("Sua frase: ", texto)
# white_list(texto.upper())