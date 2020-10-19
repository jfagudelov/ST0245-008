# Profe, ese de borrar sí me atropelló del todo ;_;


import os


class Tree():
    
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def __str__(self):
        return 'Node value: {}'.format(self.data)
                
    def contains(self, node_to_search, count=1, level=False):
        if self.data == node_to_search:
            if level == False:
                return True
            else:
                return True, 'Node level: {}'.format(count)
        elif node_to_search < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(node_to_search, count+1, level)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(node_to_search, count+1, level)
  
    def insert(self, node):
        try:
            assert self.contains(node, level=False) != True
            if node < self.data:
                if self.left == None:
                    self.left = Tree(node)
                else:
                    self.left.insert(node)
            else:
                if self.right == None:
                    self.right = Tree(node)
                else:
                    self.right.insert(node)
        except AssertionError:
            print('The value {} already exists in the tree!'.format(node))
            return None

    def find_childs(self):
        if (self.left == None) & (self.right == None):
            return 0
        elif (self.left != None) ^ (self.right != None):
            return 1
        else:
            return 2
       
    def in_order(self):
        if self.left != None:
            return self.left.in_order()
        print(self)
        if self.right != None:
            return self.right.in_order()
    
    def pre_order(self):
        print(self)
        if self.left != None:
            return self.left.pre_order()
        if self.right != None:
            return self.right.pre_order()
    
    def pos_order(self):
        if self.left != None:
            return self.left.pos_order()
        if self.right != None:
            return self.right.pos_order()
        print(self)
    
    def drop(self, node_to_del):
        if self.data == node_to_del:
            return None
        elif node_to_del < self.data:
            return self.left.drop(node_to_del)
        else:
            return self.right.drop(node_to_del)

tree = Tree(None)

while True:
    os.system('cls')
    print('Arbol ABB')
    opc = input("\n1.-Insert node \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Find \n6.-Drop \n7.-Exit \n\nSelect an option -> ")
    
    if opc == '1':
        node = input('\nNode to insert -> ')
        if tree.data == None:
            tree = Tree(int(node))
            os.system('echo Node {} inserted!'.format(int(node)))
        elif node.isdigit():
            tree.insert(int(node))
            print('Node {} inserted!'.format(int(node)))
        else:
            print('\nInsert only numerical values!')
    
    elif opc == '2':
        if tree.data == None:
            print('The tree is empty')
        else:
            print('Printing in-orden')
            tree.in_order()
    
    elif opc == '3':
        if tree.data == None:
            print('The tree is empty')
        else:
            print('Printing pre-orden')
            tree.pre_order()
    
    elif opc == '4':
        if tree.data == None:
            print('The tree is empty')
        else:
            print('Printing post-orden')
            tree.pos_order()
    
    elif opc == '5':
        if tree.data == None:
            print('The tree is empty')
        else:
            node_to_search = int(input('\nInsert node to search -> '))
            print('Searching {} . . .'.format(int(node)))
            print(tree.contains(node_to_search, level=True))

    elif opc == '6':
        if tree.data == None:
            print('The tree is empty')
        else:
            node_to_del = input('\nInsert node to delete -> ')
            if node_to_del.isdigit():
                tree.drop(int(node_to_del))
                print('{} has been deleted'.format(node_to_del))
            
    elif opc == '7':
        print('\nEOF!')
        os.system('pause')
        break
    
    else:
        print('\n Invalid option!')
