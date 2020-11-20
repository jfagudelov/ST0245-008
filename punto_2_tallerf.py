class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack():

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.size = 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

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

    def empty_reverse(self):
        new_stack = Stack()
        while self.is_empty() == False:
            new_stack.push(self.pop())
        return new_stack
    
    # Hallar promedio
    def find_average(self):
        current = self.head
        d_sum = 0
        while current.next != None:
            d_sum += current.data
            current = current.next
        return d_sum/self.size
    
    def print_stack(self):
        aux = self.head
        while aux != None:
            print('{}'.format(aux))
            aux = aux.next
           
mi_pila = Stack()
mi_pila.push(11)
mi_pila.push(22)
mi_pila.push(33)
mi_pila.push(44)
mi_pila.find_average()
mi_pila.print_stack() 
