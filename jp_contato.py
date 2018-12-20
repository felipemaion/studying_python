import re

class Contato:
    def __init__(self, nome="", telefone="", email=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    # Se chamar print(objeto) irá imprimir conforme isso:
    def __str__(self):
        return "Nome: {}\nTelefone: {}\nE-mail: {}".format(self.nome,self.telefone, self.email)
    
    def ligar(self):
        print("Ligando para {} no número {}".format(self.nome,self.telefone))
        # Uma função para ligar... (será q isso é tarefa do contato??)


    # Se perguntar objeto.nome irá retornar isso:
    @property
    def nome(self):
        return self._nome
    # etc..
    @property
    def telefone(self):
        return self._telefone
    @property
    def email(self):
        return self._email
        
    # Se fizer objeto.nome = "Bla" irá rodar isso:
    @nome.setter
    def nome(self, n):
        self._nome = n

    @telefone.setter
    def telefone(self, tel):
        self._telefone = tel

    # Se fizer objeto.email = "email" ele irá verificar se o email é valido:
    @email.setter
    def email(self, em):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", em):
            self._email = ""
            if em == "": # necessário caso crie um objeto vazio, para não mostrar o erro.
                return False
            print("Erro: E-mail inválido.")
            return False
        else:
            self._email = em
            return self._email 









