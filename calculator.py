x = input("enter first number")
y = input("enter second number")

sign = input("enter an operator")

if sign == '+':
    print(x + y)
elif sign == '*':
    print(x * y)
elif sign == '-':
    print(x - y)
elif sign == ('/'):
    print(x / y)
else:
    print("invalid operand")
