__author__ = 'alexmcneill'


class Node:

    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        #  Setting up nodes key and value
        self.key = key
        self.value = value

        #  Setting up references to keep track of where the node is in the tree
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        # Checking if the node has a parent and if the nod is its parent's left child
        return self.parent and self is self.parent.left_child

    def is_right_child(self):
        # Checking if the node has a parent and if the nod is its parent's right child
        return self.parent and self is self.parent.right_child

    def is_root(self):
        # Checking that the node doesnt have a parent
        return self.parent is None

    def is_leaf(self):
        # Checking that the node doesnt have a left or a right child
        return not (self.left_child or self.right_child)


class BasicTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        """Public put method for adding a new node to the tree"""
        if self.root is None:
            # if there is no root node making the new node the root
            self.root = Node(key, value)
        else:
            # If there is already a root node calling the private put method to find new nodes place
            self._put(key, value, self.root)

        self.size += 1

    def _put(self, key, value, current_node):
        """Private method that recursively finds a place for the new node"""
        if key > current_node.key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = Node(key, value, parent=current_node)
        else:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = Node(key, value, parent=current_node)

    def get(self, key):
        if self.root:
            found_node = self._get(key, self.root)
            if found_node:
                return found_node.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node=None):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def is_empty(self):
        return self.root is None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # Returning the iterator of the root so the user can iterate through whole tree