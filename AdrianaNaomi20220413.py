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
            self.nome = input('Informe o seu Nome:\t')
            self.idade = int(input('Informe a sua Idade:\t'))
            self.sexo = input('Informe o seu Sexo M/F:\t')[0].upper()
            if self.sexo not in 'MF':
                raise ValueError
        except:
            print("\tERRO:\n\t\tEntre com um número inteiro para idade.\n\t\tM ou F para o sexo.")
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
        print(f"\n\tPessoa: {nova_pessoa} adicionada com sucesso!\n")
        r = str (input ('\tDeseja Continuar?(Enter=S) [S/N] ')).upper() or 'S'
    # INPUT: (descomente o código abaixo, e mude r para 'N')
    # pessoas.append(Pessoa("Felipe", 36, "M"))
    # pessoas.append(Pessoa("Mirella", 38, "F"))
    # pessoas.append(Pessoa("Livia", 8, "F"))
      
    # OUTPUT:
    # Grupo: ['Felipe, M, 36 anos', 'Mirella, F, 38 anos', 'Livia, F, 8 anos']
    # A pessoa mais velha é : Mirella, F, 38 anos
    # A pessoa mais nova é : Livia, F, 8 anos
    # A média de idade do grupo é : 27.333333333333332
    # Quantos homens tem mais de 30 anos : 1
    # Quantas mulheres tem menos de 18 anos : 1
    print('\nGrupo:', *pessoas, sep="\n\t")
    print ('\nA pessoa mais velha é :\t', max(pessoas))
    print ('A pessoa mais nova é :\t' , min(pessoas))
    print(f"A média de idade do grupo é :\t { sum(pessoas) / len(pessoas) } anos")
    print('Quantos homens tem mais de 30 anos :\t', len([pessoa for pessoa in pessoas if pessoa.sexo == 'M' and pessoa.idade > 30]))
    print('Quantas mulheres tem menos de 18 anos :\t', len([pessoa for pessoa in pessoas if pessoa.sexo == 'F' and pessoa.idade < 18]))
    
if __name__ == '__main__':
    main()


      



	
	
	
