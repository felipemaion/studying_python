# a = "oi tudo bem".upper().split()
# b = input("> ").upper()
# b1 = b.split()
# b2 = b.strip()
# print(a)
# print(b1)
# print(b2)
#
# if any(x in a for x in b1):
#     print("sim")
# else:
#     print("não")
#
# if a in b1:
#     print("sim2")
# else:
#     print("não2")


def interface():
    print("="*38)
    print("Olá, bem vindo")
    print("="*38)
interface()
def text():
    frase = input("->").upper().split()
    return frase
frase = text()
def white_list(frase):
    words = "porra caralho desgraça merda droga puta filha da puta".upper().split()
    if any(x in frase for x in words):
        print("sim")
    else:
        print("não")
white_list(frase)