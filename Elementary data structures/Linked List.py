class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None #la data suivante

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data): #ajouter
        new_node = node(data)
        cur = self.head
        
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self): 
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total

    def display(self): #afficher
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data) #on ajoute avec la fonction append, la data du noeud courrant
        print(elems)

    def get(self, index): #getter
        if index>=self.length():
            print("ERROR : Index out of range ")
            return None
        cur_indx = 0
        cur_node = self.head
        while True:
            
            cur_node=cur_node.next
            if cur_indx==index:
                print(cur_node.data)
                return
            cur_indx+=1

    def erase(self,index):
        if index>=self.length():
            print("ERROR : 'Erase' index out of range")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node #on raccorde le dernier avec le prochain noeud
            cur_node = cur_node.next
            if cur_index==index: 
                last_node.next = cur_node.next
                return
            cur_index+=1

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(19)
my_list.append(7)

print("My linked list :")
my_list.display()

print("the element at the index 2 : ")
my_list.get(2)

my_list.display()

my_list.erase(2)

my_list.display()