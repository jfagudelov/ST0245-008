class Alumn():  
    
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        
    def __str__(self):
       return 'Name: {} - Age: {} - Hobbies: {}'.format(self.name,self.age,self.hobbies)

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
my_pile.stack(Alumn('Julian Andres Mazo Zapata', 17, ['toca guitarra','juega videojuegos','dibuja','lee filosofia']))
my_pile.stack(Alumn('Daniel Gonzales Bernal', 29, ['trabaja en suramericana','ve series y anime','juega videojuegos','le gusta cocinar','es calvo.']))
my_pile.stack(Alumn('Jose Miguel Blanco Velez', 20, ['jugar videojuegos','escuchar musica','estudiar','le gusta gorillaz','eminem','alcolirykoz']))
my_pile.stack(Alumn('Daniel Garcia Salcedo', 18, ['videojuegos','escuchar musica y freestyle','ver series y animes']))
my_pile.stack(Alumn('Salomon Velez Perez', 18, ['escribir','jugar videojuegos','ver anime','escuchar musica.']))
my_pile.stack(Alumn('Jose Miguel Blanco Velez', 18, ['escucha trap americano', 'jugar videojuegos', 'ver streamings en twitch']))
my_pile.stack(Alumn('Donovan Castrillon Franco', 18, ['jugar videojuegos', 'ver anime', 'jugar baloncesto', 'escuchar todo tipo de musica', 'escuchar todo tipo de musica', 'NO LE GUSTA LA MUSICA']))
my_pile.stack(Alumn('Simon Gomez Arango', 17, ['le gusta el campo y meditar', 'le gusta lo paranormal', 'tiene mala memoria', 'leer', 'escuchar musica', 'ver series y peliculas']))
my_pile.stack(Alumn('Cristian Camilo Zapata Garcia', 18, ['ama el picante', 'le encanta la musica', 'le gusta visitar lugares desconocidos', 'jugar videojuegos']))
my_pile.stack(Alumn('Santiago Parra Mejia', 16, ['es apacionado por la musica', 'toca piano', 'le gustan las matematicas puras', 'es un catolico apasionado', 'le gusta la iglesia', 'le gusta cocinar']))
my_pile.print_stack()
