# Sam Cole
# This is the driver for Liked list
from DoubleLinkedList import DoubleLinkedList

test = DoubleLinkedList()
print(test)

test.push_head(23)
test.push_head(34)
test.push_end(22)
print(test)
test.pop_end()
test.pop_head()
print(test)
