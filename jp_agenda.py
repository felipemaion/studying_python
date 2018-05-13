from jp_contato import Contato

class Agenda:
    def __init__(self, descricao=""):
        self.descricao = descricao
        self.contatos = []
    
    def adicionar(self, *contatos:Contato):
        for contato in contatos:
            self.contatos.append(contato)

    def remover(self, info):
        for i, contato in enumerate(self.contatos):
            if contato.nome == info or contato.telefone == info or contato.email == info or i == info:
                print("\n\tApagando o contato:\n{}".format(contato))
                del self.contatos[i]
                return True
        print("Contato não encontrado")
        return False
    
    def remover_todos(self):
        while self.contatos != []:
            self.remover(self.contatos[0].nome)

    def __str__(self):
        my_agenda = "\tAgenda: {}\n".format(self.descricao)
        for i, contato in enumerate(self.contatos):
            my_agenda += "ID: {}\n{}\n\n".format(i,contato)
        return my_agenda




