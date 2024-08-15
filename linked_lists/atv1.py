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

    def append(self,data):
        new = Node(data,None)
        self.end.next = new
        self.end = new

    def search(self,data):
       current = self.head.next 
       while(current.content != None):
        if current.content == data:
            return True
        current = current.next
        return False
    
    def remove(self,data):
        current = self.head.next
        previous = self.head
        while(current != None):
            if (current.content == data):
                previous.next = current.next
                current.next = None
            previous = current
            current = current.next
        if(self.end.content == data):
            self.end = previous
    
    def index(self,data):
        index = 0
        current = self.head.next
        while(current != None):
            if(current.content == data):
                return index
            else: 
                index = index + 1
                current = current.next
        if(self.end.content != data):
            return None
    
    def clear(self):
        current = self.head.next
        while(current != None):
            current.content = None
            current = current.next
    
    def count(self, data):
        count = 0
        current = self.head.next
        while(current != None):
            if(current.content == data):
                current = current.next
                count = count + 1
            elif(current.content != data):
                current = current.next
        return count

list = List()
list.append(1)
list.append(1)
list.append(1)
list.append(2)
print(list.count(1))
