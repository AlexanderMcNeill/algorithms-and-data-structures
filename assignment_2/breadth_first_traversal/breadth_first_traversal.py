__author__ = 'alexmcneill'
import Queue


def create_breadth_first_traversal_list(input_tree):
    """Method that outputs a list that is created from a breadth first traversal of given tree"""

    # Returning none if the tree is empty
    if input_tree.is_empty:
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
        for c in current_node.children:
            queue.put(c)

    return output