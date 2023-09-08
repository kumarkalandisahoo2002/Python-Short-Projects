#designing a calculator that perform aritnmatic operations

num1 = input("Enter your first operand:")
num2 = input("Enter your second operand:")

operator = input("Enter a appropiate operator(+,-,*,/,%) :: ")

if operator == '+':
    print(int(num1) + int(num2))
elif operator == '-':
    print(int(num1) - int(num2))
elif  operator == '*':
    print(int(num1) * int(num2))
elif  operator == '/':
    print(int(num1) / int(num2))
elif  operator == '%':
    print(int(num1) % int(num2))
else:
    print("Choose an appropriate Arithmatic operator")

