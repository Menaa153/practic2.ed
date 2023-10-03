from DoubleNode import DoubleNode


class DoubleList:
    
    def __init__(self):
        self.Head = None # primer nodo de la lista
        self.Tail = None # ultimo nodo de la lista
        self.Size = 0 # El tamaño de la lista que mantiene el número de nodos en la colección
    
    
    def size(self):
        return self.Size
    
    def isEmpty(self):
        return self.Size==0
    
    def first(self):
        return self.Head
    
    def last(self):
        return self.Tail
    
    def append(self, Data):
        new_node = DoubleNode(Data)
        if self.Head is None:
            self.Head = new_node
            self.Tail = new_node
        else:
            new_node.setPrev(self.Tail)  # Debes llamar al método setPrev para establecer el nodo previo.
            self.Tail.setNext(new_node)  # Debes llamar al método setNext para establecer el siguiente nodo.
            self.Tail = new_node
        self.Size += 1
    
    def addFirst(self, dato):
        newDato = DoubleNode(dato)
        if self.isEmpty():
            self.Head = newDato
            self.Tail = newDato
        else:
            newDato.setNext(self.Head)
            self.Head.setPrev(newDato)
            self.Head = newDato
        self.Size += 1
    
    
    def addLast(self, dato):
        newDato = DoubleNode(dato)
        if self.isEmpty():
            self.Head = newDato
            self.Tail = newDato
        else:
            self.Tail.setNext(newDato)
            newDato.setPrev(self.Tail)
            self.Tail = newDato
        self.Size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self.Head
            self.Head = temp.Next
            if self.Head is not None:
                self.Head.Prev = None
            else:
                self.Tail = None
            temp.Next = None
            self.Size -= 1
            return temp.getData()
    
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self.Tail
            self.Tail = temp.Prev
            if self.Tail is not None:
                self.Tail.Next = None
            else:
                self.Head = None
            temp.Prev = None
            self.Size -= 1
            return temp.getData()
    
    def remove(self, nodo):
        if nodo == self.Head:
            return self.removeFirst()
        elif nodo == self.Tail:
            return self.removeLast()
        else:
            e = nodo.getData()
            temp_prev = nodo.getPrev()
            temp_Next = nodo.getNext()
            
            temp_prev.setNext(temp_Next)
            temp_Next.setPrev(temp_prev)
            
            nodo.setNext(None)
            nodo.setPrev(None)
            self.Size -= 1
            return e
    
    
    def search_node(self, target_Data):
        current = self.Head
        while current is not None:
            if current.getData() == target_Data:
                #print(current.getPrev())
                #print(current.getNext())
                return current  # Se encontró un nodo con el valor deseado
            
            current = current.getNext()
        return None  # No se encontró un nodo con el valor deseado
    
    def addBefore(self, nodo, e):
        if nodo is None:
            return None

        if nodo == self.Head:
            self.addFirst(e)
        else:
            nuevo_nodo = DoubleNode(e)
            temp_prev = nodo.getPrev()
            temp_prev.setNext(nuevo_nodo)
            nuevo_nodo.setPrev(temp_prev)
            nuevo_nodo.setNext(nodo)
            nodo.setPrev = nuevo_nodo
            self.Size += 1
    
    def addAfter(self, nodo, e):
        if nodo is None:
            return None
        if nodo == self.Tail:
            self.addLast(e)
        else:
            nuevo_nodo = DoubleNode(e)
            temp_Next = nodo.getNext()
            nodo.setNext(nuevo_nodo)
            nuevo_nodo.setPrev(nodo)
            nuevo_nodo.setNext(temp_Next)
            temp_Next.setPrev=nuevo_nodo
            self.Size += 1
    
    # Sirve solo si la lista esta ordenada, sino el dato se agrega a Tail
    def sortList(self, dato):
        if self.isEmpty():
            self.addFirst(dato)
        else:
            temp = self.first()
            while temp is not None and dato > temp.getData():
                temp = temp.getNext()
            if temp is None:
                self.addLast(dato)
            else:
                self.addBefore(temp, dato)

    
    
    def removeDupli(self):
        temp = self.first() #Toma la cabeza de la lista
        while temp != None:
            NextNodo = temp.getNext() #toma el nodo siguiente a temp
            if NextNodo != None and temp.getData() == NextNodo.getData():
                self.remove(NextNodo)
            else:
                temp = temp.getNext()
    
    
    
    
    
    #imprimir lista
    def display(self):
        current = self.Head 
        while current:
            print(current.getData())
            current = current.getNext()
    
    
    
    
    
    #metodos para mergesort
    def split_linked_list(linked_list):
        # Divide la lista en dos mitades y devuelve las dos mitades
        fast_ptr = linked_list.Head
        slow_ptr = linked_list.Head
        
        while fast_ptr.Next is not None and fast_ptr.Next.Next is not None:
            fast_ptr = fast_ptr.Next.Next
            slow_ptr = slow_ptr.Next
            
        left_half = linked_list
        right_half = DoubleList()
        right_half.Head = slow_ptr.Next
        slow_ptr.Next = None
        right_half.Tail = linked_list.Tail
        linked_list.Tail = slow_ptr
        
        return left_half, right_half
    
    def merge_sort_linked_list(self):
        # Función principal de Merge Sort para lista doblemente enlazada
        if self.Head is None or self.Head.getNext() is None:
            return self  # La lista está vacía o tiene un solo elemento, ya está ordenada
        
        # Divide la lista en dos mitades
        left_half, right_half = self.split_linked_list()
        
        # Recursivamente ordenar ambas mitades
        left_half = left_half.merge_sort_linked_list()
        right_half = right_half.merge_sort_linked_list()
        
        # Combina las mitades ordenadas
        sorted_list = self.merge_linked_lists(left_half, right_half)
        
        return sorted_list


    def merge_linked_lists(self, left, right):
        # Combina dos listas ordenadas y devuelve la lista combinada
        merged = DoubleList()
        left_ptr = left.Head
        right_ptr = right.Head
        
        while left_ptr is not None and right_ptr is not None:
            if left_ptr.Data < right_ptr.Data:
                merged.append(left_ptr.Data)
                left_ptr = left_ptr.Next
            else:
                merged.append(right_ptr.Data)
                right_ptr = right_ptr.Next
                
        while left_ptr is not None:
            merged.append(left_ptr.Data)
            left_ptr = left_ptr.Next
            
        while right_ptr is not None:
            merged.append(right_ptr.Data)
            right_ptr = right_ptr.Next
            
        return merged

