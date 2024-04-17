
a = input("What would be the first number of the sequence: ")
b = input("What would be the second number of the sequence: ")
c = input("How many times would you like to run this: ")

def fib(a, b, c):
    list = [a, b]
    for i in range(c):
        fib_num = list[-1] + list[-2]
        list.append(fib_num)
    print(list)

if a.isdigit() and b.isdigit() and c.isdigit():
    fib(int(a), int(b), int(c))
else:
    print("Those are not digits!")





