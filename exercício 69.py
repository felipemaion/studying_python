#-*-coding:utf8;-*-
#qpy:3
#qpy:console
cot = cot2 = cot3 = cot4 = 0
while True:
    cot += 1
    print("=====REGISTRE UMA PESSOA=====")
    ida = int(input("Qual sua idade?: "))
    while True:
        sex = str(input("Qual seu sexo[F/M]: "))
        if "M" in sex or "F" in sex:
            break
    resp = str(input("Quer continuar?: ")).upper()
    if sex == "M":
        cot3 += 1
    if ida > 18:
        cot2 += 1
    if sex == "F" and ida < 20:
        cot4 += 1
    if resp == "NÃO":
        break
print(f"""Informações:
Houveram {cot} cadastros
Houveram {cot2} pessoas maiores de 18 anos
Houveram {cot3} homens cadastrados
Houveram {cot4} mulheres menores de 20 anos""")

        
    
