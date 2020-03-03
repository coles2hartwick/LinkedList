# Sam Cole
# the double linked list


class DoubleNode:
    def __init__(self, prev= None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self,value):
        new_node = DoubleNode(data = value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None

    def push_end(self,value):
        new_node = DoubleNode(data = value)
        new_node.next = None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_head(self):
        curr = self.head
        self.head = curr.next
        curr.next.prev = None
        return curr.data

    def pop_end(self):
        curr = self.tail
        curr.prev.next = None
        self.tail = curr.prev
        return curr.data
