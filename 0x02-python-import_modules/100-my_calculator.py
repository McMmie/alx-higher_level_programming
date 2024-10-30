#!/usr/bin/python3

import sys
import calculator_1 as calc

operators = ['+', '-', '*', '/']
print(sys.argv[2])

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if str(sys.argv[2]) not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a, b = int(sys.argv[1]), int(sys.argv[3])

match sys.argv[2]:
    case '+':
        print(f'{a} + {b} = {calc.add(a, b)}')
    case '-':
        print(f'{a} - {b} = {calc.sub(a, b)}')
    case '*':
        print(f'{a} * {b} = {calc.mul(a, b)}')
    case '/':
        print(f'{a} / {b} = {calc.div(a, b)}')
