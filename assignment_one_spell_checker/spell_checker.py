__author__ = 'alexmcneill'
from collections import OrderedDict
import string


class SpellChecker:
    """Class that gives you spelling recommendations based on a given string"""

    WORDS_FILE = "words.txt"
    CACHESIZE = 200

    def __init__(self):
        self.words = self.create_words_set(self.WORDS_FILE)
        self.common_mistakes = OrderedDict()
        self.orderedWords = self.create_ordered_words_dict(self.words)

    def create_words_set(self, file_location):
        """Create words set from given file
        :rtype : set
        """
        words_file = open(file_location, 'r')

        return set([line.rstrip().lower() for line in words_file])

    def create_ordered_words_dict(self, words):
        """Create dict that has a int key that points to a set of words of that length
        :rtype : dict
        """

        ordered_words = {}

        for word in words:
            key = len(word)
            if key not in ordered_words:
                ordered_words[key] = set()

            ordered_words[key].add(word)

        return ordered_words

    def cache_mistake(self, input_string, corrections):
        """Method that caches the mistake"""
        self.common_mistakes[input_string] = CachedMistake(corrections)

        #  When the common mistakes dict gets too big removing the least common mistake from the dict
        if len(self.common_mistakes) > self.CACHESIZE:
            least_common_key = None

            for key, item in self.common_mistakes:
                if least_common_key is None or item.count < self.common_mistakes[least_common_key].count:
                    least_common_key = key

            self.common_mistakes.pop(least_common_key)



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
            corrections = self.swapped_characters(input_string) | self.missing_character(input_string) | self.inserted_character(input_string) | self.incorrect_character(input_string)
            self.cache_mistake(input_string, corrections)
            return corrections

    def swapped_characters(self, incorrect_word):
        """Method returns true if the incorrect string could be the word in a different order
        :rtype : list
        """

        if len(incorrect_word) in self.orderedWords:
            possible_words = self.orderedWords[len(incorrect_word)]
            return possible_words.intersection(self.create_swapped_characters_set(incorrect_word))

        return set()

    @staticmethod
    def create_swapped_characters_set(incorrect_word):
        s = set()

        for i in range(0, len(incorrect_word)-1):
            temp_word = ""
            temp_word += incorrect_word[:i]
            temp_word += incorrect_word[i+1]
            temp_word += incorrect_word[i]
            temp_word += incorrect_word[i+2:]
            s.add(temp_word)

        return s

    def inserted_character(self, incorrect_word):

        if len(incorrect_word) in self.orderedWords:
            possible_words = self.orderedWords[len(incorrect_word)+1]
            return possible_words.intersection(self.create_inserted_character_set(incorrect_word))

        return set()

    @staticmethod
    def create_inserted_character_set(incorrect_word):
        s = set()
        for i in range(0, len(incorrect_word)+1):
            for c in string.ascii_lowercase+"'":
                s.add(incorrect_word[:i] + c + incorrect_word[i:])

        return s

    def missing_character(self, incorrect_word):
        """Method returns true if the incorrect word could be the word with a missing character
        :rtype : list
        """

        if len(incorrect_word) in self.orderedWords:
            possible_words = self.orderedWords[len(incorrect_word) - 1]

            return possible_words.intersection(self.create_missing_character_set(incorrect_word))

        return set()

    @staticmethod
    def create_missing_character_set(incorrect_word):

        s = set()

        for i in range(0, len(incorrect_word)):
            s.add(incorrect_word[:i] + incorrect_word[i+1:])

        return s

    def incorrect_character(self, incorrect_word):
        """Method returns true if the incorrect word could be the word with one incorrect character
        :rtype : list
        """

        if len(incorrect_word) in self.orderedWords:
            possible_words = self.orderedWords[len(incorrect_word)]
            return set(filter(lambda x: self.check_incorrect_character(incorrect_word, x), possible_words))

        return set()


    @staticmethod
    def check_incorrect_character(incorrect_word, possible_word):
        incorrect_count = 0

        for i in range(0, len(incorrect_word)):
            if incorrect_word[i] != possible_word[i]:
                incorrect_count += 1

        return incorrect_count < 2


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
