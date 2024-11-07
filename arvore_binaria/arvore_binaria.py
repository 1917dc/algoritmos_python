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

    def delete(self, value):
        if not self.exists(value):
            return False
        
        
        

    def get_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current.key
    
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current.key
 
node = Node(4)

node.insert(2)
node.insert(3)
node.insert(5)
node.insert(7)
node.insert(1)
