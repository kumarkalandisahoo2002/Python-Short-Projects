#finding greater among the four numbers

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
num3 = int(input("Enter the third number:\n"))
num4 = int(input("Enter the fourth number:\n"))

if num1 == num2 == num3 == num4:
    print("All the four Numbers are same.")
else:
    if num1 > num2:
        if num1 > num3:
            if num1 > num4:
                print(f"number {num1} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
            else:
                print(f"number {num4} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
        else:
            if num3 > num4:
                print(f"number {num3} is greatest among all the four numbers{num1},{num2},{num3},{num4}")  
            else:
                print(f"number {num4} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
                
    else:
        if num2 > num3:
            if num2 > num4:
                print(f"number {num2} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
            else:
                print(f"number {num4} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
        else:
            if num3 > num4:
                print(f"number {num3} is greatest among all the four numbers{num1},{num2},{num3},{num4}")  
            else:
                print(f"number {num4} is greatest among all the four numbers{num1},{num2},{num3},{num4}")
            