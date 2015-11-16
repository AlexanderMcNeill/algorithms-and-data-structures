__author__ = 'alexmcneill'
import Queue
import copy

class WordNode():

    def __init__(self, ):
        pass


class WordLadder():

    WORDS_FILE = "words.txt"

    def __init__(self):
        # Creating a dictionary for creating word ladders with
        self.dict = self.create_words_set(self.WORDS_FILE)

    def create_words_set(self, file_location):
        """Create words set from given file
        :rtype : set
        """
        # Reading in the words file
        words_file = open(file_location, 'r')

        # Returing a set with spaces removed and each of the words to lowered
        return set([line.rstrip().lower() for line in words_file])

    def create_word_ladder(self, first_word, second_word):
        # Creating root node
        root = self.create_node(first_word, None, None)

        # Getting a copy of the dict for this ladder
        words = copy.deepcopy(self.dict)

        # Creating queue with the the root node in it
        queue = Queue.Queue()
        queue.put(root)

        # Creating variable for keeping track of the found node
        found_node = None

        # Breadth-first traversal/creation of the word tree
        while not queue.empty() and found_node is None:
            # Getting the next node from the queue and getting its children
            current_node = queue.get()
            current_node["children"] = self.get_children(current_node, words)

            for c in current_node["children"]:
                # Checking if any of the children are the second word
                if c["word"] == second_word:
                    found_node = c
                # Adding the children to the queue to be processed
                queue.put(c)
                # Removing word from the words set so it isn't processed again
                words.remove(c["word"])

        # Returning the result of the ladder
        if found_node is not None:
            return self.create_path_string(found_node)  # Returning a string representation of the ladder

        else:
            return "No path found"

    def get_children(self, parent, words):
        output = []

        # Adding any words that could be a child of the parent to the output
        for w in words:
            if self.is_possible_child(parent["word"], w):
                output.append(self.create_node(w, parent, None))

        return output

    @staticmethod
    def create_node(word, parent, children):
        return {"word": word, "parent": parent, "children": children}

    @staticmethod
    def is_possible_child(start_word, new_word):
        differences = 0

        # Iterating through the characters checking that there is only one difference between the words
        for i in range(0, len(start_word)):
            if start_word[i] != new_word[i]:
                differences += 1
            if differences > 1:
                return False

        return True

    @staticmethod
    def create_path_string(node):
        current_node = node
        path_list = []

        # Creating a list to represent the path by following each nodes parent to the root
        while current_node is not None:
            path_list.append(current_node["word"])
            current_node = current_node["parent"]

        # Returning a readable string
        return "<-".join(path_list)

if __name__ == "__main__":
    word_ladder = WordLadder()
    print(word_ladder.create_word_ladder("virus", "scout"))