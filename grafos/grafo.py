class Graph:
    def __init__(self):
        # variável da classe que armazena um dicionário
        # contendo todas as vértices do grafo e seus vizinhos
        self.adj_list = dict()

    def print(self):
        graph_str = ""

        for node, neighbours in self.adj_list.items():
            if len(neighbours) == 0:
                neighbours = "{None}"
            graph_str += (f"{node} -> {neighbours} \n")
        return graph_str


    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise Exception("O valor já existe dentro do Grafo.")
    
    def remove_node(self, node):
        if node not in self.adj_list:
            return Exception("O valor não existe dentro do Grafo.")
        
        for neighbours in self.adj_list.values():
            neighbours.discard(node)
        
        self.adj_list.remove(node)


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
        pass

            
graph = Graph()

graph.add_node(3)
graph.add_node(5)
graph.add_node(4)

graph.add_edge(3,4)


print(graph.print())
graph.remove_edge(3,4)
print(graph.print())