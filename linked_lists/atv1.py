class Node:
    def __init__(self,content,next=None):
        self.content = content
        self.next = next

class LinkedList:
    def __init__(self,content,next):
        self.content = content
        self.next = next


# uma lista nesse caso tem um início e um fim, por isso assimilamos uma head e um end
class List:
    def __init__(self):
        self.head = Node(-1,None)
        self.end = self.head
    
    def print(self):
        current = self.head.next
        while(current != None):
            print(current.content)
            current = current.next

    def append(self,x):
        new = Node(x,None)
        self.end.next = new
        self.end = new

    def search(self,x):
       current = self.head.next 
       while(current.content != None):
        if current.content == x:
            return True
        current = current.next
        return False
    
    def remove(self,x):
        current = self.head.next
        previous = self.head
        while(current != None):
            if (current.content == x):
                previous.next = current.next
                current.next = None
            previous = current
            current = current.next
        if(self.end.content == x):
            self.end = previous
    
    def index(self,x):
        index = 0
        current = self.head.next
        previous = self.head
        while(current != None):
            if(current.content == x):
                return index
            else: 
                index = index + 1
                current = current.next
                previous = current
        if(self.end.content != x):
            print('número inexistente')