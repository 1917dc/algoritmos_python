#    Dado um arquivo de texto de nome "inscritos.txt" contendo uma lista de nomes (string) e a categoria de atendimento (normal: 'n', ou prioritário: 'p'), com o separador vírgula em cada linha (Ex: Fulano de Tal, 'p'); implemente um código em python que leia esse arquivo e gere uma lista de atendimentos a serem realizados em um determinado órgão público. 
#    A ordem de atendimento deve ser: a cada três prioritários que saem da fila, dois normais também são atendidos e assim sucessivamente.  Ou seja, seguindo a lógica p, p, p, n, n, p, p, p, n, n,...
#    Dentro de cada categoria a ordem é a mesma lida no arquivo. 
#    Os atendimentos são realizados de meia em meia hora, começando o primeiro às 11h00 e terminando o último às 15h30, dentro de um mesmo dia, ou seja, o horário de atendimento deve ser impresso, junto com o nome e a categoria.
#    Caso a lista tenha mais nomes que a quantidade de atendimentos possíveis dentro de um dia de expediente, a solução deve imprimir o atendimento para quantos dias que forem necessários, colocando um texto "1o dia", "2o dia", ... e assim por diante, antes de listar os atendimentos de cada dia.
#    O resultado do código deve ser salvo em um arquivo de nome "ordemAtendimento.txt". Esse arquivo deve ter a lista com a ordem de atendimento com a informação do dia, do horário, do nome da pessoa e da sua categoria, em cada linha.

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
        if self.head.next is None:
            return

        if self.head.next.next is None:
            self.head.next = None
            self.end = self.head
            return

        current = self.head.next
        while current.next != self.end:
            current = current.next

        current.next = None
        self.end = current
        

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
        return self.data.last()
    
    def empty(self):
        self.data.clear()
    
    def removeLast(self):
        self.data.removeFirst()
    
    def returnFirst(self):
        self.data.printFirst()

    def print(self):
        self.data.print()
        
horario = 0
dia = 0
atendimento = True

prefList = Stack()
normList = Stack()

finalList = []

with open('inscricoes.txt', 'r', encoding='utf-8') as file:
    persons = file.readlines()
    for person in persons:
        person = person.replace("\n","").split(", ")
        if person[1] == 'n':
            normList.push(person)
        else:
            prefList.push(person)
        
while atendimento == True:
    print(f'DIA: {dia}')
    while horario < 9:
        for i in range(3):
            if(prefList.top() != -1):
                print(prefList.top())
                prefList.pop()
                horario += 1
        if horario < 8:
            for i in range(2):
                if(normList.top() != -1):
                    print(normList.top())
                    normList.pop()
                    horario += 1
        else:
            if(normList.top() != -1):
                print(normList.top())
                normList.pop()
                horario += 1
    dia += 1
    horario = 0
    if prefList.top() == None and normList.top() == None:
        atendimento = False