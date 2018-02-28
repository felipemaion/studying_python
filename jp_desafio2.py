
# Desafio 2:
# Escreva uma função que recebe uma string e uma lista de palavras proibidas e substitui a palavra proibida por *


import re # Usar Regular Expressions para ignorar Maiúsculas e afins...

def censurar(texto, *palavras):
    for palavra in palavras:
        texto = re.sub(palavra, "*"*len(palavra), texto, flags=re.IGNORECASE)
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
palavras = ["cu", "foda", "porra"]
print("Texto original:", texto)
print("Palavras a serem censuradas:", palavras)
print("\nMétodo com Regular Expression:")
print(censurar(texto, *palavras))
print("\nMétodo com String - Mudando para Upper case:")
print(censurar1(texto,*palavras))
print("\nMétodo com String - Sem mudar para Upper case:")
print(censurar2(texto,*palavras))
