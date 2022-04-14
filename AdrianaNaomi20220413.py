# Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre: 
# a) O nome da pessoa mais velha 
# b) O nome da mulher mais jovem 
# c) A média de idade do grupo 
# d) Quantos homens tem mais de 30 anos 
# e) Quantas mulheres tem menos de 18 anos'''


class Pessoa:
    def __init__(self, *args):
        if not args:
            self.nova()
        else:
            self.nome = args[0]
            self.idade = args[1]
            self.sexo = args[2]

    def nova(self):
        try:
            self.nome = input('Informe o seu Nome :')
            self.idade = int(input('Informe a sua Idade :'))
            self.sexo = input('Informe o seu Sexo M/F :')[0]
        except ValueError:
            print("Entre com um número inteiro")
            return self.nova()
        
    ## definindo as comparações: <, <=, ==, >=, >, respectivamente:
    def __lt__(self, outraPessoa):
        return self.idade < outraPessoa.idade

    def __le__(self, outraPessoa):
        return self.idade <= outraPessoa.idade

    def __eq__(self, outraPessoa):
        return self.idade == outraPessoa.idade

    def __ge__(self, outraPessoa):
        return self.idade >= outraPessoa.idade

    def __gt__(self, outraPessoa):
        return self.idade > outraPessoa.idade
    
    ## definindo a soma de pessoas e inteiros. pessoa + pessoa ou pessoa + inteiro:
    def __radd__(self, outraPessoa):
        if type(outraPessoa) == Pessoa:
            return self.idade + outraPessoa.idade
        if type(outraPessoa) == int:
            return self.idade + outraPessoa
        
    ## definindo como imprimir a pessoa:
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.idade} anos"
    
    def __repr__(self):
        return f"'{self.__str__()}'"    


def main():
    r = 'S'
    pessoas = []
    while r == 'S':
        nova_pessoa = Pessoa()
        pessoas.append(nova_pessoa)
        print(f"\n\tPessoa: {nova_pessoa} adicionada com sucesso!")
        r = str (input ('Deseja Continuar?(Enter=S) [S/N] ')).upper() or 'S'
    # pessoas.append(Pessoa("Felipe", 36, "M"))
    # pessoas.append(Pessoa("Mirella", 38, "F"))
    # pessoas.append(Pessoa("Livia", 8, "F"))
    print('Grupo:', pessoas)
    print ('A pessoa mais velha é :', max(pessoas))
    print ('A pessoa mais nova é :' , min(pessoas))
    print('A média de idade do grupo é :', sum(pessoas) / len(pessoas))
    print('Quantos homens tem mais de 30 anos :', len([pessoa for pessoa in pessoas if pessoa.sexo == 'M' and pessoa.idade > 30]))
    print('Quantas mulheres tem menos de 18 anos :', len([pessoa for pessoa in pessoas if pessoa.sexo == 'F' and pessoa.idade < 18]))
    
if __name__ == '__main__':
    main()


      



	
	
	
