import sys


def calculator(a, b):
    if b == 0:
        quotient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quotient = a / b
        remainder = a % b
    return (a + b, a - b, a * b, quotient, remainder)


if len(sys.argv) != 3:
    print("InputError: bad number of arguments")
    print("Usage: python operations.py <number1> <number2>")
    exit()

a1 = sys.argv[1]
a2 = sys.argv[2]
x = 2

try:
    a1 = int(a1)
except ValueError:
    x -= 1
try:
    a2 = int(a2)
except ValueError:
    x -= 1
if (x == 2):
    r = calculator(a1, a2)
    print("Sum: ", r[0])
    print("Difference: ", r[1])
    print("Product: ", r[2])
    print("Quotient: ", r[3])
    print("Remainder: ", r[4])
else:
    print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")

