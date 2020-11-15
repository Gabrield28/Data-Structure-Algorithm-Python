class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         print(self.items[len(self.items)-1])

     def size(self):
         print(len(self.items))

myStack = Stack()
myStack.push(3)
myStack.push(6)
myStack.push(38)
print("taille de la pile ")
myStack.size()
print("dernier element ajoute a la pile ")
myStack.peek()