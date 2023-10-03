
class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
    
    def getData(self):
        return self.Data
    def setData(self, Data):
        self.Data = Data
    
    
    def getNext(self):
        return self.Next
    def setNext(self, Next):
        self.Next = Next
    
    def __str__(self):
        return str(self.Data)