__author__ = 'alexmcneill'
from spell_checker import SpellChecker

spell_checker = SpellChecker()

def check_line(input_line, line_index):
    words = input_line.translate(None, ".,?!").split()
    for word in words:
        word = word.lower()
        corrections = spell_checker.check(word)
        if corrections is not None:
            if word not in corrections:
                print("Incorrect word on line {}: {}, Possible corrections: {}".format(line_index, word, corrections))

        else:
            print("Incorrect word on line {}: {}, Possible corrections: {}".format(line_index, word, "None found"))


if __name__ == "__main__":

    input_file_path = raw_input("Enter the path of the file you want to check: ")
    valid_file = False
    input_file = None

    while not valid_file:
        try:
            input_file = open(input_file_path, 'r')
            valid_file = True
        except IOError:
            print("File entered was invalid")
            input_file_path = input("Enter the path of the file you want to check: ")

    current_line = input_file.readline()
    line_index = 0

    while current_line != "" and current_line is not None:
            check_line(current_line, line_index)
            current_line = input_file.readline()
            line_index += 1