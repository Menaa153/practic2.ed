from ListSimple import ListSimple

class Queue:
    def __init__(self):
        self.data = ListSimple()
        
    def isEmpty(self):
        return self.data.Size==0
    
    def size(self):
        return len(self.data)
    
    def enqueue(self, data):
        self.data.addLast(data)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.data.removeFirst()
    
    def first(self):
        return self.data.first()
    
    def display(self):
        current = self.data.Head
        while current:
            print(current.getData())
            current = current.getNext()
            
    def __iter__(self):
        current = self.data.Head
        while current:
            yield current.getData()  # Utiliza el método getData() para obtener los datos del nodo actual
            current = current.getNext()

"""q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q.first())
elemento = q.dequeue()

print("Elemento desencolado:", elemento)
print("Tipo de elemento:", type(elemento))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())"""