from jp_agenda import *

print("\nCriando os contatos...")
felipe = Contato(nome="Felipe Maion", telefone="(11) 98585-6949", email="felipe.maion@gmail.com")
levi = Contato("Levi","+55 63 8496-8506","")
lucas = Contato("Lucas","+55 11 94157-6259", "") 
thinker = Contato("Thinker","+556792429709")
jp = Contato("João Pedro", "+55 75 8129-0525")

print("\nCriando a agenda...")
agenda = Agenda("Grupo Python & C++ POO - Aulas")

print("\nAdicionando contatos um a um à agenda...")
agenda.adicionar(felipe)
agenda.adicionar(levi)
agenda.adicionar(lucas)
agenda.adicionar(thinker)
agenda.adicionar(jp)

print("\nContatos adicionado! Veja a agenda:\n",agenda)
print("__________________________")

print("\nRemovendo todos os contatos...")
agenda.remover_todos()
print("\nContatos removidos! Veja a agenda:\n",agenda)
print("__________________________")

print("\nAdicionando vários contatos de uma só vez...")
agenda.adicionar(felipe,levi,lucas,thinker,jp)
print(agenda)

