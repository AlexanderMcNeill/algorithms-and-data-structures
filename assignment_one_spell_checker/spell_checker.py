__author__ = 'alexmcneill'


class SpellChecker:

    WORDS_FILE = "words"

    def __init__(self):
        self.words = self.create_words_set(self.WORDS_FILE)

    def create_words_set(self, file_location):
        """Create words set from given file"""
        words_file = open(file_location, 'r')
        words = set()

        current_word = words_file.readline()
        while current_word != "":
            words.add(current_word.rstrip())
            current_word = words_file.readline()

        return words

    def check(self, input_string):
        """perform a spell check on the input string with respect the words set"""
        if input_string in self.words:
            return [input_string]
        else:
            return self.recommend_correct_spelling(input_string)

    def recommend_correct_spelling(self, input_string):
        """Recommend all possible corrections in the words set"""
        """Must be able to handle common spelling mistakes like:
        -swapping adjacent characters
        -inserting a single character
        -deleting a single character
        -replacing a single character
        -(Extra challenge: consider phonetic substitutions as well)"""
        pass


test = SpellChecker()