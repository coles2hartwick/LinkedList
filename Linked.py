# Sam Cole
# This is the linked list class


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data


    def remove_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data


    def clear(self):
        self.head = None


    def search(self, search):
        current_node = self.head
        while current_node.next:
            if current_node == search:
                return current_node


    def remove(self, search):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
            if current_node == search:
                previous_node = current_node.next
