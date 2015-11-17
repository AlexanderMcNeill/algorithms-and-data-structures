__author__ = 'alexmcneill'


class ReversibleLinkedList:

    class _Node:

        def __init__(self, data, next_element):
            self.data = data
            self.next = next_element

    def __init__(self):
        # Setting up setting up variables to keep track of the head and tail
        self._head = None
        self._tail = None

        # Setting up variable to keep track of the size
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError
        return self._head.data

    def enqueue(self, data):
        new_node = self._Node(data, None)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def dequeue(self):
        # Raising error if you try to dequeue with a empty list
        if self.is_empty():
            raise IndexError

        # Getting the data from the head and updating the head with its next
        output = self._head.data
        self._head = self._head.next

        # Updating the size
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return output

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

    def __str__(self):
        output = []

        current_node = self._head

        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next

        return str(output)


if __name__ == "__main__":
    linked_list = ReversibleLinkedList()

    for i in range(0, 100):
        linked_list.enqueue(i)

    print(linked_list)

    linked_list.reverse_list()

    print(linked_list)