# Escreva um programa que calcule o preço a pagar pelo fornecimento 
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
# lação: R para residências, I para indústrias e C para comércios. Calcule o preço a 
# pagar de acordo com a tabela a seguir. 
# Preço por tipo e faixa de consumo 
# Tipo Faixa (kWh) Preço 
# Residencial Até 500 R$ 0,40 
# Acima de 500 R$ 0,65 
# Comercial 
# Até 1000 R$ 0,55 
# Acima de 1000 R$ 0,60 
# Industrial 
# Até 5000 R$ 0,55 
# Acima de 5000 R$ 0,60
def input_usuario():
    try:
        kWh = float(input("Informe a quantidade de kWh consumida: "))
        tipo = input("Informe o tipo de instalação: R para residências, I para indústrias e C para comércios: ")[0].upper()
        return kWh, tipo
    except ValueError:
        print("Números apenas")
        input_usuario()
        
def calcular_consumo(kWh, tipo):
    if tipo == 'R':
        if kWh <= 500:
            return kWh*0.4
        else:
            return kWh*0.65
    elif tipo == 'C':
        if kWh <= 1000:
            return kWh*0.55
        else:
            return kWh*0.6
    elif tipo == 'I':
        if kWh <= 5000:
            return kWh*0.55
        else:
            return kWh*0.6
    else:
        print("Tipo de instalação inválida")
        return 0
        
def main():
    kWh, tipo = input_usuario()
    print(f"O valor a pagar é R${calcular_consumo(kWh, tipo):.2f}")
    
    
if __name__ == '__main__':
    main()