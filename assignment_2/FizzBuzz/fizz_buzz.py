__author__ = 'alexmcneill'


FIZZ_NUM = 3
BUZZ_NUM = 5


def check_fizz(input_num):
    return input_num % FIZZ_NUM == 0


def check_buzz(input_num):
    return input_num % BUZZ_NUM == 0


def get_fizz_buzz(input_num):
    output = ""
    if check_fizz(input_num) or check_buzz(input_num):
        if check_fizz(input_num):
            output += "Fizz"
        if check_buzz(input_num):
            output += "Buzz"
    else:
        output += str(input_num)
    return output

if __name__ == "__main__":
    for i in range(1, 100):
        print(get_fizz_buzz(i))