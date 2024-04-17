import math


def rounding():
    user_input = input("How many digits of e would you like to see: ")
    if user_input.isdigit():
        print(round(math.e, int(user_input)))
    else:
        print("Please enter a valid digit!")
        return rounding()


rounding()
