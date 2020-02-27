# Sam Cole
# This is the driver for Liked list
from Linked import LinkedList

lst = LinkedList()
print(lst)

lst.add_to_head(14)
print(lst)
lst.add_to_head(13)
print(lst)
lst.add_to_end(55)
lst.add_to_end(22)
print(lst)
lst.remove_head()
print(lst)
lst.remove_end()
print(lst)
lst.clear()
print(lst)
lst.add_to_head(14)
lst.add_to_head(13)
lst.add_to_end(55)
lst.add_to_end(22)
print(lst)
print(lst.search(55))
lst.delete_node(22)
print(lst)
