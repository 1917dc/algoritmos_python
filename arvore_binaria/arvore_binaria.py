# fazer a classe Node definindo as partes da esquerda e direita do nó

class Node:
    def __init__(self, value):
        self.key = value

        # definindo as pontas da árvore
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        