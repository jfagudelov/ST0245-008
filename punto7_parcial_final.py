class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack():

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

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

    # Respuesta punto
    def empty_reverse(self):
        new_stack = Stack()
        while self.is_empty() == False:
            new_stack.push(self.pop())
        return new_stack
    
    def print_stack(self):
        aux = self.head
        while aux != None:
            print('{}'.format(aux.data))
            aux = aux.next
            
mi_pila = Stack()
mi_pila.push(11)
mi_pila.push(22)
mi_pila.push(33)
mi_pila.push(44)
mi_pila.print_stack()

inverted_pile = mi_pila.empty_reverse()
print(mi_pila.is_empty())
inverted_pile.print_stack()
