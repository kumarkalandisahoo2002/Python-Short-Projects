num1 = int(input("Enter your first number:\n"))
num2 = int(input("Enter your second number:\n"))
num3 = int(input("Enter your third number:\n"))

if num1 == num2 == num3:
    print("All the three Numbers are same.")
else:
    if num1 > num2:
        if num1 > num3:
            print(num1, f"is the greatest among three numbers {num1},{num2},{num3}.")
        else:
            print(num3, f"is the greatest among three numbers {num1},{num2},{num3}.")
    else:
        if num2 > num3:
            print(num2, f"is the greatest among three numbers {num1},{num2},{num3}.")
        else:
            print(num3, f"is the greatest among three numbers {num1},{num2},{num3}.")
    