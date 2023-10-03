class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, dato):
        new_node = Node(dato)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Datos existentes en forma de lista
existing_data = [["Mike", 1105], ["Rob", 750], ["Paul", 720], ["Ana", 660], ["Rose", 500], ["Jack", 510]]

# Crear una instancia de la lista enlazada
my_list = LinkedList()

# Agregar los datos existentes a la lista enlazada usando addFirst
for data in existing_data:
    my_list.addFirst(data)

newdata=["Jeni", 740]
my_list.addFirst(newdata)

# Mostrar la lista enlazada
my_list.display()  # Esto mostrará la lista enlazada en el orden en que se agregaron los datos


