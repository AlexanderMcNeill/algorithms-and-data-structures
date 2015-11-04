__author__ = 'alexmcneill'

START = 1
END = 100
FIZZ_NUM = 3
BUZZ_NUM = 5

for i in range(START, END+1):
    fizz = i % FIZZ_NUM
    buzz = i % BUZZ_NUM
    output = ""
    if fizz == 0 or buzz == 0:
        if fizz == 0:
            output += "Fizz"
        if buzz == 0:
            output += "Buzz"
    else:
        output += str(i)

    print(output)