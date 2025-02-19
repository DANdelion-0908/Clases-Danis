number1 = 1
number2 = 0

try:
    result = number1 / number2
except ZeroDivisionError:
    print("ERROR: División por cero.")