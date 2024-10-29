# fazer um algoritmo de busca de árvore binária


#definir a node que será usada na árvore

class Node:
    def __init__(self, value):

        self.key = value

        self.left = None
        self.right = None

    def insert(self, value):
        if(self.key == None):
           self.key = value

        if(self.key == value):
            return

        if(self.key < value):
            if(self.right == None):
                self.right = Node(value)

            else:
                cmp = self.right
                while(cmp.key != None):
                    if(cmp.key < value):
                        cmp = cmp.right

                    elif(cmp.key > value):
                        cmp.left = Node(value)
                    
                self.right = Node(value)

node = Node(2)
print(node.key)
node.insert(3)
print(node.right.key)
node.insert(4)