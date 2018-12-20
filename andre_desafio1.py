print("Cadastro Identidade")
name = input("Digite seu nome:\n").upper()
age = input("Digite sua idade:\n").upper()
address = input("Digite seu endereço:\n").upper()
father = input("Nome do pai:\n").upper()
mother = input("Nome da mãe:\n").upper()
profession = input("Qual sua profissão:\n").upper()
## Para testes:
# name = "Teotônio Parrudo Garrido Golias Galante Lacerda Pedroso Peixoto Cardoso Carvalho Cabral Cavalcante".upper()
# age = "100000"
# address = "Rua dos Bobos nº 0".upper()
# father = "Mr Catra (Wagner Domingues Costa)".upper()
# mother = "Leontina Albino".upper()
# profession = "O Gigante".upper()

# Define o tamanho do box que será feito:
box = 40
# Precisando de uma linha extra?
line_break = ("","")

# Define os textos e campos que será mostrado:
fields = [line_break,
          ("CARTEIRA DE IDENTIDADE".center(box-3,"_"), ""),
          line_break,
          ("NOME:",name),
          ("IDADE:",age),
          line_break,
          ("ENDEREÇO:",address),
          line_break,
          ("FILIAÇÃO:",""),
          ("-",father),
          ("-",mother),
          line_break,
          ("PROFISSÃO:",profession),
          line_break,
          line_break,
          line_break,
          ("JUNDIAI/SP".center(box-3),""),
          line_break]

# Desenha a caixa (box) com os campos (fields) dentro, dimensionados):
def draw_box(fields, box):
    print("╔".ljust(box,"═") + "╗")
    for txt,variable in fields:
        print("║" +
              " {} {}".format(txt, variable[:(box - len(txt) - 3)]).ljust(len(txt), " ") +
              "║".rjust(box - 2 - len(txt) - len(variable[:(box - len(txt) - 3)])," "))
    print("╚".ljust(box,"═") + "╝")


draw_box(fields,box)