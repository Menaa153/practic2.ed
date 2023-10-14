from Node import Node
from ListSimple import ListSimple


class StackList:
    def __init__(self):
        self.data = ListSimple()
    
    def size(self):
        return self.data.getSize()
    
    def isEmpty(self):
        return self.size==0
    
    def push(self, data):
        self.data.addFirst(data)
    
    def pop(self):
        return self.data.removeFirst()
    
    def top(self):
        if not self.isEmpty():
            return self.data.first().getData()
        else: return None

"""# Ejemplo de uso:
stack = StackList()  # Crear una pila con capacidad 5
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


print("Tamaño de la pila:", stack.size())  # Debería imprimir 3
print("Elemento eliminado del tope:", stack.pop())  # Debería imprimir 3
print("Elemento en el tope:", stack.top())  # Obtener el elemento en la parte superior sin cambiar stack.top"""