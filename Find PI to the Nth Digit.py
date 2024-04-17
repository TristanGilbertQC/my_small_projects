import math


def rounding():
    user_input = input("How many digits of pi would you like to see: ")
    if user_input.isdigit():
        print(round(math.pi, int(user_input)))
    else:
        print("Please enter a valid digit!")
        return rounding()


rounding()
