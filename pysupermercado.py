# coding: utf-8
# Codigo feito por: FELIPE MAION GARCIA
# Data: 14/2/2018

# Vou fazer esse código em português só pq vc falou q não fala inglês.


class Carrinho:
    # O initi definirá  o que a classe Carrinho sabe ao ser criada!
    # Cada self.VARIAVEL define uma variável específica de cada OBJETO!!
    def __init__(self, dono = None):
        self.dono = dono # Veja que cada dono do carrinho tem seu nome...
        self.produtos = [] # seus produtos
        self.quantidade = 0 # a quantidade total
        self.preco_total = 0.00 # e a conta total
        print("====="*10)
        print("|| Novo cliente!! \n|| Bem vindo {} ao Python's Supermercado".format(self.dono))
        print("=====" * 10)

    ## APARTIR DAQUI serão criados os métodos que a CLASSE Carrinho sabe fazer!!
    ## OBS: Quando falamos de objetos é sempre importante ter em mente:
    ## O QUE O OBJETO SABE??
    ## O QUE O OBJETO FAZ??

    ## O que ele sabe foi definido no init (sabe quem é o dono, sabe os produtos, a qntdade, e o preço_total)

    # O que ele faz? Adiciona produto, qual é o mais caro (q tanto), o mais barato (q tanto), e fecha o total.

    # Adiciona o nome do produto, com o preço na quantidade informada ou 1.:
    def adiciona_produto(self, nome, preco, quantidade=1):
        try:
            preco = float(str(preco).replace(",", ".")) # Caso o preço seja com Virgula, troca para ponto.
            quantidade = int(quantidade)
            for _ in range(quantidade): # Caso coloque mais de UM desse produto de uma vez...
                self.produtos.append([str(nome), preco])
                self.quantidade += 1
                self.preco_total += preco
            print("\t{0} adicionou {1} x '{2}' por R${3:.2f}/un. ao carrinho de compras".format(self.dono,
                                                                                                quantidade,
                                                                                                nome, preco))
            return True
        except:
            print("!!Não foi possível adicionar {} x {} por {} ao carrinho do {} \tPreço \
             ou Quantidade inválidos".format(quantidade,nome,preco,self.dono))
            return False

    # Os dois métodos abaixo (mais_caro e mais_barato), como o nome diz, acham o mais caro e o mais barato! rs!
    # Porém, se algum valor for informado, ele procurará os produtos acima (ou abaixo) do valor informado.
    # se nenhum valor for informado, ele procura o maximo (ou minimo) da lista.

    def mais_caro(self, valor=None):
        try:
            caros = []
            if valor:
                for produto, preco in self.produtos:
                    if preco >= valor:
                        caros.append("{0} por R${1:.2f}".format(produto,preco))
                print("Produtos do {0} acima de R${1:.2f}: {2}".format(self.dono, valor, caros))
                return caros
            caro = max(self.produtos,key = lambda preco: preco[1])
            print("Produto mais caro do/a {0} foi o {1[0]} por R${1[1]:.2f}".format(self.dono, caro))
            return caro
        except:
            print("{}, não achei produtos mais caros no seu carrinho.".format(self.dono))


    def mais_barato(self, valor=None):
        try:
            baratos = []
            if valor:
                for produto, preco in self.produtos:
                    if preco <= valor:
                        baratos.append("{0} por R${1:.2f}".format(produto, preco))
                print("Produtos do {0} abaixo de R${1:.2f}: {2}".format(self.dono, valor, baratos))
                return baratos
            barato =  min(self.produtos,key = lambda preco: preco[1])
            print("Produto mais barato do {0} foi o {1[0]} por R${1[1]:.2f}".format(self.dono, barato))
            return barato
        except:
            print("{}, não achei produtos mais baratos no seu carrinho".format(self.dono))
            return None

    # Passa no caixa... fecha a conta... passa a régua...
    # Tchau!

    def passa_no_caixa(self):
        print("-----"*10)
        print("| {0} gastou \tR${1:.2f} em \t{2} produtos.".format(self.dono, self.preco_total, self.quantidade))
        print("| OBRIGADO, {} VOLTE SEMPRE!! ".format(self.dono.upper()))
        print("-----"*10)
        return self.preco_total

## EXEMPLO DE USOS:

# Esse if __name__ == "__main__" serve para só rodar isso aqui se o arquivo for rodado direto.
# Caso esse arquivo seja importado como um modulo em outra aplicação essa parte não será executada.

if __name__ == "__main__":
    #### Um pouco de frescura:
    print("\n")
    print("*****"*15)
    print("\t*** PYTHON'S SUPERMERCADO - ONDE COMPRAR BARATO É SUPERFULO\t ***")
    print("*****"*15)
    print("\n")

    # Cria o primeiro cliente, PEDRO
    pedro = Carrinho("Pedro")
    pedro.adiciona_produto("Papel higiênico", "2") # Adiciona produto. Preço é STRING!!
    pedro.adiciona_produto("Butijão de Gás", 7000.01) # Adiciona produto. Preço é FLOAT!
    felipe = Carrinho("Felipe") # Outro cliente pegou um carrinho!
    # Adiciona com quantidade, e informando exatamente, sem importar a oderm:
    felipe.adiciona_produto(quantidade=2, preco=200, nome="Achocolatado")  # Preco Inteiro
    felipe.adiciona_produto("Café", 2000,2) # Sem informar importa a ordem.
    felipe.passa_no_caixa() # Felipe não perde tempo e vai embora....
    pedro.adiciona_produto("Feijão", "50,2", 2) # Pedro continua nas compras. PRECO COM VIRGULA (string)!!
    pedro.adiciona_produto("Feijão", "50.2", 2) # Preco com ponto e string.
    pedro.adiciona_produto("Café", 2000) # Cafézinho básico...
    pedro.adiciona_produto(preco=20.00, nome="Filtro") # Precisa comprar Filtro tb...
    pedro.mais_barato() # O que foi O mais barato do Pedro??
    pedro.mais_barato(1000) # O que custou menos que 1000?
    pedro.mais_caro() # O Mais caro?
    pedro.mais_caro(1000) # O que custou mais de 1000?
    pedro.passa_no_caixa() # Fecha a conta caloteiro...
    print("\n")

    ## Agora no esquema que vc estava fazendo de looping, até string em branco.
    maria = Carrinho("Maria")
    while True:
        produto = input("Produto: ")
        if not produto: break
        preco = input("Preço: R$")
        try:  # coloquei esse try só pq se der um espaço e enter não funcionava! Rs!
            # Funcionaria sem... mas aí varias vezes o produto não entraria no carrinho..
            # tenho mania de mandar uns  espaços!
            quantidade = int(input("Quantidade [Enter = 1]: "))
        except:
            print("\t... quantidade definida como 1")
            quantidade = 1
        maria.adiciona_produto(produto,preco,quantidade)

    maria.mais_caro()
    maria.mais_barato()
    maria.passa_no_caixa()