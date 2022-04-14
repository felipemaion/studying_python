# Authou: Felipe Maion

# - grafo com 1500 nós
# - nem todos os pontos se conectam (sparse)
# - cada conexão tem um peso

# Restrições:
# - Partida em A, chegada em B
# - Comprimento < N

# Tarefa:
# - encontrar o com mínimo custo (min soma pesos)

# create grapho

class Node:
    def __init__(self, id):
        self.id = id
        self.connections = {}

    def add_connection(self, node, weight):
        self.connections[node] = weight

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return f'{self.id}'

class Grapho:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        self.nodes[id] = Node(id)

    def add_connection(self, id_node_a, id_node_b, weightAB, directional=True):
        self.nodes[id_node_a].add_connection(self.nodes[id_node_b], weightAB)
        if not directional:
            self.nodes[id_node_b].add_connection(self.nodes[id_node_a], weightAB)
    

    def __str__(self):
        return f'{self.nodes}'

    def __repr__(self):
        return f'{self.nodes}'
    
# grafo = { "A" : ["B"],
#           "B" : ["C", "D"],
#           "C" : ["B", "E"],
#           "D" : ["A"],
#           "E" : ["B"]
#         }
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")


grapho = Grapho()
grapho.add_node(nodeA)
grapho.add_node(nodeB)
grapho.add_connection(nodeA, nodeB, 10)
print(grapho)