

class ArrayStack:
    def __init__(self, capacity):
        self.data = []
        self.top = -1
    
    def size(self):
        return self.top +1
    
    def isEmpty(self):
        return size()==0
    
    def push(self, data):
        if self.top < self.data.len-1:
            self.top+=1
            self.data[self.top] = data
        else:
            print("Stack overflow")
    
    def pop(self):
        if isEmpty():
            temp=self.data[self.top]
            self.data[self.top]=None
            self.top -= 1
        else:
            return None
    
    def top(self):
        if isEmpty():
            return self.data[self.top]
        else: return None