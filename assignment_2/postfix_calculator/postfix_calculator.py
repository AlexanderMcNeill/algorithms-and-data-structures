__author__ = 'alexmcneill'


total = 0
stack = []
operators = {"*": lambda x, y: x * y, "+": lambda x, y: x + y, "/": lambda x, y: x / y, "%": lambda x, y: x % y
                ,"-": lambda x, y: x - y}

current_input = raw_input()

for c in current_input:
    if c in operators:
        # Getting the left and right hand of the equation
        right_hand = stack.pop()
        left_hand = stack.pop()

        # Calculating new value and adding it to the stack
        stack.append(operators[c](left_hand, right_hand))
    else:
        # Adding new value to the stack
        stack.append(int(c))


print(stack)
