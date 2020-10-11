import random as rd

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class SinglyLinkedList():
    
    def __init__(self):
        self.head = None
    
    def __len__(self):
        current = self.head
        if self.is_empty():
            return 0
        else:
            cont = 1
            while current.next != None:
                current = current.next
                cont += 1
            return cont    
        
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    
    def is_empty(self):
        return 1 if self.head == None else 0
    
    def insert(self, new_node):
        node_to_insert = Node(new_node)
        if self.head == None:
            self.head = node_to_insert
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node_to_insert
            
    def reverse(self, n_rotations):
        assert self.is_empty() != 1
        assert n_rotations >= 0
        if n_rotations == 0:
            return self.head
        elif n_rotations > len(self):
            return self.reverse(n_rotations%len(self))
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = self.head
            self.head = tail
            n_tail = self.head
            while n_tail.next != self.head:
                n_tail = n_tail.next
            n_tail.next = None
            return self.reverse(n_rotations-1)
                   
list_a = SinglyLinkedList()
for i in range(1, 11):
    list_a.insert(Node(i))
list_a.print_list()
rotations = rd.randint(0, 100002)
print('The list will rotate:', rotations, 'times')
list_a.reverse(rotations)
print('Rotated list:')
list_a.print_list()
