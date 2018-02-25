class Candidato:
	def __init__(self, nome):
		self.nome = nome
		self.votos = 0
	
	def votar(self):
		self.votos += 1

	def __str__(self):
		return "Candidato: {} com {} votos apurados.".format(self.nome, self.votos)


class Eleicao:
	def __init__(self, *candidatos):
		self.candidatos = {}
		# self.fim = False
		for candidato in candidatos:
			self.candidatos[candidato] = Candidato(candidato)
			
	def votar(self, candidato):
		if candidato in self.candidatos.keys():
			# print("\n")
			self.candidatos[candidato].votar()
			self.inicio()
		else:
			self.fim()

	def inicio(self):
		print("\n")
		for nome, candidato in self.candidatos.items():
			print("Candidato: {}".format(nome))
		voto = input("Votar em: ")
		self.votar(voto)

	def fim(self):
		print("\n\t\tApuração Eleitoral:")
		for candidato in self.candidatos:
			print(self.candidatos[candidato])


####### CHAMADA DO PROGRAMA E CRIAÇÃO DE OBJETOS:

##### Método 1:

print("\tEleição 1 -  Safe Creation! ")
print("\t\tDefinição de Pleito:")
candidatos = ["Felipe", "Pedro", "Diogo", "Rafa", "Gláucio", "Luciano"]
print("Número de Candidatos: " + str(len(candidatos)))
eleicao = Eleicao(*candidatos)
eleicao.inicio()

##### Método 2:

# print("\n\tEleição 2 - Safe Validation and Except\n")
invalida = False
class CandidatoInvalidoException(Exception):
	pass
while not invalida:
	try:
		print("\n\tEleição 2 - Safe Validation and Except\n")
		candidatos = []
		print("\t\tDefinição de Pleito:")
		num_candidato = int(input("Número de candidatos: "))
		for i in range(num_candidato):
			candidato = input("Nome Candidato: ")
			if candidato != "" and candidato not in candidatos:
				candidatos.append(candidato)
			else:
				raise CandidatoInvalidoException()
		print("\t\tVotação:")
		eleicao = Eleicao(*candidatos)
		eleicao.inicio()
		invalida = True
		break
	except ValueError:
		print("Entre com um número válido.")
	except CandidatoInvalidoException:
		print("Candidato não pode ser sem nome, nem com nome repetido.\n")
		print("Reiniciando processo eleitoral... \n\n")
	except KeyboardInterrupt:
		invalida = True
		print("\n\nSolicitação de encerramento das Eleições 2 pelo Usuário.")


##### Método 3:

print("\n\t Eleição 3 - Non safe!!")
candidatos = []
print("\t\tDefinição de Pleito:")
num_candidato = input("Número de candidatos: ")
for i in range(int(num_candidato)):
	candidatos.append(input("Nome Candidato:"))
print("\t\tVotação:")
eleicao = Eleicao(*candidatos)
eleicao.inicio()

			
			
			
			
			
			
			
			
			