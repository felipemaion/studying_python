import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "_main_":
    clear_screen()
print("Bem vindo")
def pergunta():
    perg = str(input("""Qual sua pergunta?
-->\033[92;1m """)).strip().upper()
    return perg
def resposta(pergunta):
    print("\033[mProcessando...")
    if "VOCÊ ESTÁ BEM?" in pergunta:
        print("Resposta:\033[94;1m Ótimo!\033[m")
    else:
        print("Sem respostas")
clear_screen()

resposta(pergunta())


def minha_entrada():
    entrada_valida = False
    while not entrada_valida:
        try:
            a = float(input("A>"))
            b = float(input("B>"))
            c = float(input("C>"))
            entrada_valida = True
        except ValueError:
            print("Porra mas vc é burro pra porra...")
    return a,b,c

a,b,c = minha_entrada()

print("a:{} b:{} c:{}".format(a,b,c))
#dlt = delta(a,b,c)



