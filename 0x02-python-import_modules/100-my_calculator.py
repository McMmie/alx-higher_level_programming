#!/usr/bin/python3

if __name__ == '__main__':

    import sys
    import calculator_1 as calc

    operators = ['+', '-', '*', '/']

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if str(sys.argv[2]) not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    operatr = sys.argv[2]
    b = int(sys.argv[3])

    if operatr == '+':
        print(f'{a} + {b} = {calc.add(a, b)}')
    elif operatr == '-':
        print(f'{a} - {b} = {calc.sub(a, b)}')
    elif operatr == '*':
        print(f'{a} * {b} = {calc.mul(a, b)}')
    elif operatr == '/':
        print(f'{a} / {b} = {calc.div(a, b)}')
