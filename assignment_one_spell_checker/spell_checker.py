__author__ = 'alexmcneill'


class SpellChecker:
    """Class that gives you spelling recommendations based on a given string"""

    WORDS_FILE = "words"

    def __init__(self):
        self.words = self.create_words_set(self.WORDS_FILE)
        self.common_mistakes = {}

    def create_words_set(self, file_location):
        """Create words set from given file
        :rtype : set
        """
        words_file = open(file_location, 'r')
        words = set()

        #  Reading through the first line of the file to start the reading
        current_word = words_file.readline()

        while current_word != "":
            words.add(current_word.rstrip())
            current_word = words_file.readline()

        return words

    def check(self, input_string):
        """Method performs a spell check on the input string with respect the words set and returns a list of possible
        corrections
        :rtype : bool
        """
        if input_string in self.words:
            return [input_string]
        elif input_string in self.common_mistakes:
            return self.common_mistakes[input_string].corrections
        else:
            corrections = self.recommend_correct_spelling(input_string)
            self.cashe_mistake(input_string, corrections)
            return corrections

    def recommend_correct_spelling(self, input_string):
        """Recommend all possible corrections to the input string that are in the words set
        :rtype : set
        """

        # Creating a set to contain the possible corrections for the input string
        corrections = set()

        # Checking each word to see if it is a possible correction to the input string
        for word in self.words:
            if self.is_possible_correction(input_string, word):
                corrections.add(word)

        return corrections

    def cashe_mistake(self, input_string, corrections):
        """Method that cashes the mistake. Maybe used to retain order of the dict later"""
        self.common_mistakes[input_string] = corrections

    def is_possible_correction(self, incorrect_word, word):
        """Method that checks if the input word could be a correction for the input incorrect word
        :rtype : bool
        """
        swapped_check_result = self.check_swapped_characters(incorrect_word, word)
        missing_check_result = self.check_missing_character(incorrect_word, word)
        incorrect_check_result = self.check_incorrect_character(incorrect_word, word)
        phonetic_check_result = self.check_phonetic_substitution(incorrect_word, word)

        #  Returning true if any of the checks were correct
        return swapped_check_result or missing_check_result or incorrect_check_result or phonetic_check_result

    def check_swapped_characters(self, incorrect_word, word):
        """Method returns true if the incorrect string could be the word in a different order
        :rtype : bool
        """
        return len(incorrect_word) == len(word) and sorted(incorrect_word) in sorted(word)

    def check_missing_character(self, incorrect_word, word):
        """Method returns true if the incorrect word could be the word with a missing character
        :rtype : bool
        """
        return False

    def check_incorrect_character(self, incorrect_word, word):
        """Method returns true if the incorrect word could be the word with one incorrect character
        :rtype : bool
        """
        return False

    def check_phonetic_substitution(self, incorrect_word, word):
        """Method returns true if the incorrect word could be the word with a incorrect phonetic substitution
        :rtype : bool
        """
        return False


class CashedMistake:
    """Class that keeps track of the usage and corrections for a cashed mistake"""

    def __init__(self, corrections):
        self._corrections = corrections
        self.count = 1

    @property
    def corrections(self):
        """Method that gives access to the corrections set while recording how many times the correction has been
        used"""
        self.count += 1
        return self._corrections

    @corrections.setter
    def corrections(self, value):
        self._corrections = value

test = SpellChecker()
