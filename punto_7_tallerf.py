class Alumn():
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def __str__(self):
       return 'Name: {} - Age: {} - Grade: {}'.format(self.name,self.age,self.grade)

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Pile():

    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head == None

    def stack(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            nuevo_nodo= Node(data)
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo 

    def pop(self):
        if self.is_empty():
            return None
        else:
            aux = self.head
            self.head = self.head.next
            aux.next = None
            return aux.data

    def peek(self):
        return self.head.data

    def print_stack(self):
        aux = self.head
        cont = 1
        while aux != None:
            print('Alumn {}: {}'.format(cont, aux.data))
            aux = aux.next
            cont += 1

my_pile = Pile()
my_pile.stack(Alumn('Pepe', 30, 8.9))
my_pile.stack(Alumn('Alex', 27, 3.7))
my_pile.print_stack()

