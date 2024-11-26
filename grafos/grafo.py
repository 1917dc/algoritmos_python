class Graph:
    def __init__(self):
        # variável da classe que armazena um dicionário
        # contendo todas as vértices do grafo e seus vizinhos
        self.adj_list = dict()

    def print(self):
        graph_str = ""

        for node, neighbors in self.adj_list.items():
            if len(neighbors) == 0:
                neighbors = "{None}"
            graph_str += (f"{node} -> {neighbors} \n")
        return graph_str


    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise Exception("O valor já existe dentro do Grafo.")
    
    def remove_node(self, node):
        if node not in self.adj_list:
            return Exception("O valor não existe dentro do Grafo.")
        
        for neighbors in self.adj_list.values():
            neighbors.discard(node)
        
        self.adj_list.pop(node)


    def add_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        
        if to_node not in self.adj_list:
            self.add_node(to_node)
        
        self.adj_list[from_node].add(to_node)
        self.adj_list[to_node].add(from_node)
    
    def remove_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            return Exception(f"O valor {from_node} não está inserido no Grafo.")

        if to_node not in self.adj_list:
            return Exception(f"O valor {to_node} não está inserido no Grafo.")
        
        if to_node in self.adj_list[from_node] and from_node in self.adj_list[to_node]:
            self.adj_list[from_node].discard(to_node)
            self.adj_list[to_node].discard(from_node)

        else:
            return Exception(f"Não existe um vértice conectando os dois valores.")
    
    def find_shortest(self, from_node, to_node):
        if from_node not in self.adj_list:
            return Exception(f"O número {from_node} não existe no Grafo.")

        if to_node not in self.adj_list:
            return Exception(f"O número {to_node} não existe no Grafo.")
        
        # elementos que já foram visitados
        visited = set()
        # fila que armazena os elementos que ainda serão analisados
        queue = [(from_node, [from_node])]

        while queue:
            current_node, path = queue.pop(0)

            if current_node == to_node:
                return path
            
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.adj_list[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None
        
# Instanciação do grafo
graph = Graph()

# Adição de nós
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
for node in nodes:
    graph.add_node(node)

# Adição de arestas
edges = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "E"), ("B", "F"),
    ("C", "G"), ("C", "H"), ("D", "I"), ("D", "J"), ("E", "K"),
    ("F", "L"), ("G", "M"), ("H", "N"), ("I", "O"), ("J", "K"),
    ("K", "L"), ("L", "M"), ("M", "N"), ("N", "O"), ("O", "A")
]
for from_node, to_node in edges:
    graph.add_edge(from_node, to_node)

# Impressão do grafo
print("Grafo inicial:")
print(graph.print())

# Remoção de uma aresta
graph.remove_edge("A", "B")

# Impressão do grafo após remover a aresta
print("Grafo após remover a aresta entre A e B:")
print(graph.print())

# Remoção de um nó
graph.remove_node("C")

# Impressão do grafo após remover o nó
print("Grafo após remover o nó C:")
print(graph.print())

# Encontrar caminho mais curto
try:
    caminho = graph.find_shortest("A", "K")
    print(f"Caminho mais curto de A para K: {caminho}")
except Exception as e:
    print(e)

# Teste adicional para caminho mais curto
try:
    caminho = graph.find_shortest("B", "N")
    print(f"Caminho mais curto de B para N: {caminho}")
except Exception as e:
    print(e)