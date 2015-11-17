__author__ = 'alexmcneill'
import Queue
import tree

def create_breadth_first_traversal_list(input_tree):
    """Method that outputs a list that is created from a breadth first traversal of given tree"""

    # Returning none if the tree is empty
    if input_tree.is_empty():
        return None

    # Creating queue with the the root node in it
    queue = Queue.Queue()
    queue.put(input_tree.root)

    # Creating a list for the output
    output = []

    while not queue.empty():
        # Getting the next node off the queue
        current_node = queue.get()

        # Adding node's value to the output list
        output.append(current_node.value)

        # Adding each child node to the queue to be processed next
        if current_node.has_left_child():
            queue.put(current_node.left_child)
        if current_node.has_right_child():
            queue.put(current_node.right_child)

    return output

if __name__ == "__main__":
    t = tree.BasicTree()
    t.put(4, 4)
    t.put(5, 5)
    t.put(8, 8)
    t.put(3, 3)
    t.put(19, 19)
    t.put(1, 1)

    print(create_breadth_first_traversal_list(t))