from DoubleNode import DoubleNode
from DoubleList import DoubleList


data2 = [1105,750,720,660,500,500,500,510,510]

lisenzda = DoubleList()

for i in data2:
    lisenzda.addFirst(i)

"""lisenzda.display()
print("-----")
removernodo = lisenzda.search_node(660)
lisenzda.remove(removernodo)
lisenzda.removeFirst()
lisenzda.removeLast()
lisenzda.removeDupli()

lisenzda.sortList(600) # solo si la lista esta ordenada

lisenzda.addBefore(lisenzda.search_node(600),5000)
lisenzda.addAfter(lisenzda.search_node(600),4533)

lisenzda.display()"""

# Ejemplo de uso:
data2 = [1105, 999, 510, 720, 660, 500, 500, 510, 510,800]
mylist = DoubleList()
for item in data2:
    mylist.append(item)

sorted_list = mylist.merge_sort_linked_list()
# Ahora sorted_list contiene la lista ordenada
sorted_list.display()
print(sorted_list.size())


