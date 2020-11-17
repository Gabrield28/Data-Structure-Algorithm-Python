class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("ERROR : la file est vide !")
        else:
            print("Element retire de la file : ")
            print(self.items[0])
            return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            print("ERROR : la file est vide !")
        else:
            print(self.items[0])

    def size(self):
        print("taille de la file :")
        print(len(self.items))
     
    def display(self):
        print("Ensemble des elements de la file :")
        for i in range(len(self.items)):
            print(self.items[i]),
        print
    

myQueue = Queue()
myQueue.dequeue()
myQueue.enqueue(3)
myQueue.enqueue(6)
myQueue.enqueue(38)
myQueue.display()
myQueue.size()
myQueue.display()
myQueue.peek()
myQueue.dequeue()
myQueue.display()
myQueue.dequeue()
myQueue.display()