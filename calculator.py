#!/usr/bin/env python3
import sys

def usage():
    print("Usage: calculator.py <num1> <operator> <num2>")
    print("Operators: +, -, *, /")

if len(sys.argv) != 4:
    usage()
    sys.exit(1)

num1 = float(sys.argv[1])
op = sys.argv[2]
num2 = float(sys.argv[3])

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero")
        sys.exit(1)
    result = num1 / num2
else:
    usage()
    sys.exit(1)

print(result)
