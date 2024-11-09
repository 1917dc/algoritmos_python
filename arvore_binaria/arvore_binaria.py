class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

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
        if not self.key:
            return None
            
        elif value < self.key:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.key:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            if not self.left:
                return self.right
            
            if not self.right:
                return self.left
            
            min_larger = self.right.get_min()
            self.key = min_larger.key
            self.right = self.right.delete(min_larger)
        
        return self

    def get_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current
    
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current
    
class Tree:
    def __init__(self, key):
        self.root = Node(key)
    
    def insert(self, value):
        current = self.root

        while current:
            if value < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            elif value > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return
            else:
                return

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)


class MaxHeap:
    def __init__(self, key):
        self.root = Node(key)
        self.nodes = [self.root]
    
    def insert(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

        parent = self.nodes[(len(self.nodes)-2)//2]
        new_node.parent = parent

        if parent.left:
            parent.right = new_node
        else:
            parent.left = new_node

        self.heapify(new_node)
        
    def heapify(self, node):
        while node.parent and node.key > node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    def printHeap(self):
        heap_array = [node.key for node in self.nodes]
        print(heap_array)           
    
    def printRoot(self):
        if self.root:
            print(self.root.key)
        else:
            return None
    
def preorder(node):
    if node:
        print(node.key)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key)