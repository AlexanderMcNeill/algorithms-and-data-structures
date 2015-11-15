__author__ = 'alexmcneill'


class Node:

    def __init__(self, data, next_element):
        self.data = data
        self.next = next_element


class ReversibleLinkedList:

    def __init__(self):
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def reverse_list(self):
        # Setting where to start reversing
        current_node = self._head
        last_node = None

        # Looping through each node
        while current_node is not None:
            # Saving the next node
            temp_node = current_node.next

            # Reversing the current node
            current_node.next = last_node
            last_node = current_node

            # Moving to next node
            current_node = temp_node

        # Switching the head and tail
        temp_node = self._head
        self._head = self._tail
        self._tail = temp_node

    def is_empty(self):
        return self._size == 0

    def enqueue(self, data):
        new_node = Node(data, None)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def __str__(self):
        output = []

        current_node = self._head

        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next

        return str(output)


linked_list = ReversibleLinkedList()

for i in range(0, 100):
    linked_list.enqueue(i)

print(linked_list)

linked_list.reverse_list()

print(linked_list)