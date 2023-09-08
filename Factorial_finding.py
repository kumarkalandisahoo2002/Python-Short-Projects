"""finding Single Factorial of a given number using function"""

def fact(number):
    if number == 0:
        return 1
    if number >= 1:
        return number*fact(number-1)
    
num = int(input("Enter a number to find factorial:\n"))
print(f"Factorial of {num}! is: ", fact(num))



# """Finding Double-factorial of a given number using function"""
# def fact(number):
#     if number == 0 or number == -1:
#         return 1
#     if number >= 1:
#         return number * fact(number - 2)
    
# num = int(input("Enter a number: "))
# print(f"The Double-factorial value of {num}!! is: ",fact(num))



# """Finding Double-Factorial of given number using Range() function"""
# num = int(input("Enter a number: "))
# if num == 0 or num == -1:
#     print(f"The Double-Factorial of {num}!! is: ",1)
# fact = 1
# if num >= 1:
#     for i in range(num,0,-2):
#         fact *= i
#     print(f"The Double-Factorial of {num}!! is: ",fact)



# """Finding Factorial of given number using Range() function"""
# num = int(input("Enter a number: "))
# if num == 0:
#     print(f"The Factorial of {num}! is: ",1)
# fact = 1
# if num >= 1:
#     for i in range(num,0,-1):
#         fact *= i
#     print(f"The Factorial of {num}! is: ",fact)