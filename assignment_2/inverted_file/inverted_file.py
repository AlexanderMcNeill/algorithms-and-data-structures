__author__ = 'alexmcneill'


class WordNode:

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
        return self.parent and self is self.parent.left_child  # Checking if the node has a parent and if the nod is its parent's left child

    def is_right_child(self):
        return self.parent and self is self.parent.right_child # Checking if the node has a parent and if the nod is its parent's right child

    def is_root(self):
        return self.parent is None  # Checking that the node doesnt have a parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)  # Checking that the node doesnt have a left or a right child


class WordTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        """Public put method for adding a new node to the tree"""
        if self.root is None:
            # if there is no root node making the new node the root
            self.root = WordNode(key, value)
        else:
            # If there is already a root node calling the private put method to find new nodes place
            self._put(key, value, self.root)

    def _put(self, key, value, current_node):
        """Private method that recursively finds a place for the new node"""
        if key > current_node.key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = WordNode(key, value, parent=current_node)
        else:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = WordNode(key, value, parent=current_node)

    def get(self, key):
        if self.root:
            found_node = self._get(key, self.root)
            if found_node:
                return found_node.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def create_ordered_list(self):
        if self.root:
            return self._create_ordered_list(self.root)
        else:
            return None

    def _create_ordered_list(self, current_node):
        if current_node.is_leaf():
            return [{"word": current_node.key, "positions": current_node.value}]
        else:
            output = []
            if current_node.has_left_child():
                output += self._create_ordered_list(current_node.left_child)
            output += [{"word": current_node.key, "positions": current_node.value}]
            if current_node.has_right_child():
                output += self._create_ordered_list(current_node.right_child)
            return output

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


if __name__ == '__main__':

    d = ["this", "this", "is", "a", "ab", "test"]
    t = WordTree()

    for i in range(0, len(d)):
        key = d[i].lower()
        found_list = t.get(key)
        if found_list is None:
            t.put(key, [i])
        else:
            found_list.append(i)

    print(t.create_ordered_list())