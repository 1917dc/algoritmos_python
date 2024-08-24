class Node:
        def __init__(self,content,next=None):
           self.content = content
           self.next = next

class LinkedList:
        def __init__(self,content,next):
           self.content = content
           self.next = next

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

    def pop(self):
        self.remove(self.end.content)
        

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

    def last(self):
        return self.end.content

    # metodo que imprime os 5 primeiros termos da lista

    def printFirstFive(self):
        count = 0
        current = self.head.next
        while(current != None):
            if count < 5 :
                print(current.content)
                current = current.next
                count += 1
            else :
                return None

    # metodo que insere um termo na primeira posicao

    def insertAtZero(self, data):
        self.head.next = Node(data, self.head.next.next)

    # metodo que remove o primeiro elemento da lista
    def removeFirst(self):
        self.head.next = self.head.next.next

    def printFirst(self):
        return self.head.next

    # metodo que reomve numeros impares da lista
    def removeOdd(self):
        current = self.had.next
        previous = self.head
        while(current != None):
          if(current % 2 != 0):
            previous.next = current.next
          previous = current
          current = current.next

    def countAll(self):
      current = self.head.next
      count = 0
      while(current != None):
        count += 1
        current = current.next

class Stack:
    def __init__(self):
        self.data = List()
    
    def push(self,data):
        self.data.append(data)
    
    def pop(self):
        self.data.pop()
    
    def top(self):
        if self.countAll() > 0:
            return self.data.last()
    
    def empty(self):
        self.data.clear()
    
    def removeLast(self):
        self.data.removeFirst()
    
    def returnFirst(self):
        self.data.printFirst()

    def print(self):
        self.data.print()
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
print('\n')
stack.removeLast()
stack.print()