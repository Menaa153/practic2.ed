

class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None]* self.capacity  # Inicializamos el arreglo con el tamaño especificado
        self.Top = -1 # Inicializamos top en -1 ya que no hay elementos en el principio
    
    def size(self):
        return self.Top +1 
    
    def isEmpty(self):
        return self.size()==0
    
    def push(self, data):
        if self.Top < self.capacity -1:
            self.Top+=1
            self.data[self.Top] = data # Insertamos el elemento en el tope de la pila
        else:
            print("Stack overflow")
    def top(self):
        if not self.isEmpty():
            return self.data[self.Top]
        else: return None
        
    def pop(self):
        if not self.isEmpty():
            temp=self.data[self.Top]
            self.data[self.Top]=None
            self.Top -= 1
            return temp
        else:
            return None
    
        
    def __str__(self):
        return str(self.data)




# Ejemplo de uso:
stack = StackArray(5)  # Crear una pila con capacidad 5
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


print(stack)
print("Tamaño de la pila:", stack.size())  # Debería imprimir 3
print("Elemento eliminado del tope:", stack.pop())  # Debería imprimir 3
print("Elemento en el tope:", stack.top())  # Obtener el elemento en la parte superior sin cambiar stack.top



