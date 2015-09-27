__author__ = 'alexmcneill'
from collections import OrderedDict

class SpellChecker:
    """Class that gives you spelling recommendations based on a given string"""

    WORDS_FILE = "words"
    CACHESIZE = 50

    def __init__(self):
        self.words = self.create_words_set(self.WORDS_FILE)
        self.common_mistakes = OrderedDict()

    def create_words_set(self, file_location):
        """Create words set from given file
        :rtype : set
        """
        words_file = open(file_location, 'r')
        words = set()

        #  Reading through the first line of the file to start the read in loop
        current_word = words_file.readline()

        while current_word != "":
            words.add(current_word.rstrip())  # Adding word that is stripped of spacing and new line characters
            current_word = words_file.readline()

        return words

    def check(self, input_string):
        """Method performs a spell check on the input string with respect the words set and returns a list of possible
        corrections
        :rtype : set
        """
        if input_string in self.words:
            corrections_set = set()
            corrections_set.add(input_string)
            return corrections_set
        elif input_string in self.common_mistakes:
            return self.common_mistakes[input_string].corrections
        else:
            corrections = self.recommend_correct_spelling(input_string)
            self.cache_mistake(input_string, corrections)
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

    def cache_mistake(self, input_string, corrections):
        """Method that caches the mistake"""
        self.common_mistakes[input_string] = CachedMistake(corrections)

        #  When the common mistakes dict gets too big removing the least common mistake from the dict
        if len(self.common_mistakes) > self.CACHESIZE:
            self.common_mistakes = OrderedDict(sorted(self.common_mistakes.items(), key=lambda t: t[1].count))
            self.common_mistakes.popitem(True)
            pass


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

    @staticmethod
    def check_swapped_characters(incorrect_word, word):
        """Method returns true if the incorrect string could be the word in a different order
        :rtype : bool
        """
        return len(incorrect_word) == len(word) and sorted(incorrect_word) == sorted(word)

    @staticmethod
    def check_missing_character(incorrect_word, word):
        """Method returns true if the incorrect word could be the word with a missing character
        :rtype : bool
        """
        if len(incorrect_word) == len(word) - 1:
            for c in incorrect_word:
                if c not in word:
                    return False
            return True

        return False

    @staticmethod
    def check_incorrect_character(incorrect_word, word):
        """Method returns true if the incorrect word could be the word with one incorrect character
        :rtype : bool
        """

        if len(incorrect_word) == len(word):
            incorrect_count = 0

            for c in incorrect_word:
                if c not in incorrect_word:
                    incorrect_count += 1

            return incorrect_count < 2

        return False

    @staticmethod
    def check_phonetic_substitution(incorrect_word, word):
        """Method returns true if the incorrect word could be the word with a incorrect phonetic substitution
        :rtype : bool
        """
        return False


class CachedMistake:
    """Class that keeps track of the usage and corrections for a cached mistake"""

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
