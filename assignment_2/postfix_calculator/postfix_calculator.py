__author__ = 'alexmcneill'



operators = {"*": lambda x, y: x * y, "+": lambda x, y: x + y, "/": lambda x, y: x / y, "%": lambda x, y: x % y
                ,"-": lambda x, y: x - y}


def calculate(postfix_string):
    stack = []

    input = postfix_string.split(" ")

    for v in input:
        if v in operators:
            # Getting the left and right hand of the equation
            right_hand = stack.pop()
            left_hand = stack.pop()

            # Calculating new value and adding it to the stack
            stack.append(operators[v](left_hand, right_hand))
        else:
            # Adding new value to the stack
            stack.append(float(v))

    return stack.pop()

if __name__ == "__main__":
    current_input = raw_input()
    print(calculate(current_input))
