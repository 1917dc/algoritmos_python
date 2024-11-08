class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.key:
            self.key = value
        
        if self.key == value:
            return
        
        if self.key < value:
            if self.right:
                self.right.insert(value)
                return
            self.right = Node(value)
            return

        if self.key > value:
            if self.left:
                self.left.insert(value)
                return
            self.left = Node(value)
            return

    def exists(self, value):
        if self.key is value:
            return True
        
        if self.key < value:
            if self.right is None:
                return False

            return self.right.exists(value)
        
        if self.key > value:
            if self.left is None:
                return False

            return self.left.exists(value)

    # implementar método de deletar node
    def delete(self, value):
        return 
 

tree = Node(4)
tree.insert(2)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(6)

