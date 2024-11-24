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
                print(f"caminho mais curto de {from_node} até {to_node}")
                print(f"path: {path}")
                return path
            
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.adj_list[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None
        

graph = Graph()
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)

graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(3,6)
graph.add_edge(4,5)

graph.find_shortest(6, 5)