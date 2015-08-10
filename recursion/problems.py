__author__ = 'alexmcneill'


def big_number(input_list):  # Method that finds the biggest number in a list
    if len(input_list) == 1:
        return input_list[0]
    else:
        half_point = len(input_list) / 2

        first_half_result = big_number(input_list[:half_point])
        second_half_result = big_number(input_list[half_point:])

        if first_half_result > second_half_result:
            return first_half_result
        else:
            return second_half_result


numbers_string_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def string_to_int(input_string):  # method that converts a string of numbers to an int
    if len(input_string) == 1:
        # getting the int value of the character
        return numbers_string_map[input_string]
    else:
        # getting the last index of the list
        last_index = len(input_string)-1
        return string_to_int(input_string[last_index]) + string_to_int(input_string[:last_index]) * 10


test = string_to_int("16533")

print(str(test))

input_list = [1, 2, 3, 4, 5, 32, 7, 8, 9, 10]

print(big_number(input_list))