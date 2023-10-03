from Node import Node


class ListSimple:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Size = 0
    
    def getSize(self):
        return self.Size
    def setSize(self, Size):
        self.Size= Size
    
    def isEmpty(self):
        return self.Size==0
    
    def first(self):
        return self.Head
    
    def last(self):
        return self.Tail
    
    def addFirst(self, dato):
        newDato = Node(dato)
        if self.isEmpty():
            self.Head = newDato
            self.Tail = newDato
        else:
            newDato.setNext(self.Head)
            self.Head = newDato
        self.Size += 1
    
    
    def addLast(self, dato):
        newDato = Node(dato)
        if self.isEmpty():
            self.Head = newDato
            self.Tail = newDato
        else:
            self.Tail.setNext(newDato)
            self.Tail = newDato
        self.Size += 1
    
    def removeFirst(self):
        if not self.isEmpty():
            temp = self.Head
            self.Head = temp.getNext()
            temp.setNext(None)
            self.Size -= 1
            return temp.getData()
        else:
            return None
    
    def removeLast(self):
        if self.Size == 1:
            return self.removeFirst()
        else:
            temp = self.Tail
            anterior = self.Head
            while anterior.getNext() != self.Tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.Tail = anterior
            self.Size -= 1
            return temp.getData()
    
    def sortList(self, lis, dato):
        if lis.isEmpty():
            lis.addFirst(dato)
        else:
            temp = lis.first()
            while temp is not None and dato > temp.getData():
                temp = temp.getNext()
            if temp is None:
                lis.addLast(dato)
            else:
                lis.addBefore(temp, dato)
    
    def sortlist2(self, lis, nodo):
        if lis.isEmpty():
            lis.addLast(nodo)
        else:
            temp = lis.first()
            while temp != None and dato < temp.getData():
                temp = temp.getNext()
            if temp is None:
                li.addLast(nodo)
            else:
                lis.addBefore(temp, nodo)
        
    def display(self):
        current = self.Head
        while current:
            print(current.getData())
            current = current.getNext()
    
    #metodos para merge sort
    def merge_sort(self, key=lambda x: x[1]):
        """
        Ordena la lista utilizando el algoritmo Merge Sort, utilizando la función key para determinar la clave de ordenamiento.
        """
        if self.Size <= 1:
            return self  # La lista está vacía o tiene un solo elemento, ya está ordenada

        # Dividir la lista en dos mitades
        left_half, right_half = self.split_linked_list()

        # Recursivamente ordenar ambas mitades
        left_half = left_half.merge_sort(key)
        right_half = right_half.merge_sort(key)

        # Combinar las mitades ordenadas
        return self.merge_linked_lists(left_half, right_half, key)

    def split_linked_list(self):
        """
        Divide la lista actual en dos mitades y devuelve las dos mitades como listas separadas.
        """
        if self.Size <= 1:
            return self, None

        mid = self.Size // 2
        left_half = ListSimple()
        right_half = ListSimple()

        current = self.Head
        for i in range(mid):
            left_half.addLast(current.Data)
            current = current.Next

        while current:
            right_half.addLast(current.Data)
            current = current.Next

        return left_half, right_half

    def merge_linked_lists(self, left, right, key):
        """
        Combina dos listas enlazadas ordenadas y devuelve la lista combinada.
        """
        merged = ListSimple()
        left_ptr = left.Head
        right_ptr = right.Head

        while left_ptr and right_ptr:
            if key(left_ptr.Data) < key(right_ptr.Data):
                merged.addLast(left_ptr.Data)
                left_ptr = left_ptr.Next
            else:
                merged.addLast(right_ptr.Data)
                right_ptr = right_ptr.Next

        # Agregar los elementos restantes de las dos listas, si los hay
        while left_ptr:
            merged.addLast(left_ptr.Data)
            left_ptr = left_ptr.Next

        while right_ptr:
            merged.addLast(right_ptr.Data)
            right_ptr = right_ptr.Next

        return merged
    # ...


    # ...


