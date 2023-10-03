
class DoubleNode:
    
    def __init__(self, Data):
        self.Data = Data # El dato almacenado en el nodo
        self.Next = None # Referencia al siguiente nodo
        self.Prev = None # Referencia al nodoPrev
    
    
    def getData(self):
        return self.Data
    def setData(self, Data):
        self.Data = Data
    
    
    def getNext(self):
        return self.Next
    def setNext(self, Next):
        self.Next = Next
    
    
    def getPrev(self):
        return self.Prev
    def setPrev(self, Prev):
        self.Prev = Prev
    
    
    def __str__(self):
        return str(self.Data)