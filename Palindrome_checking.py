#checking a number is palindrome or not

number = int(input("Enter a number:\n"))
num = number
result = 0
while num != 0:
    rem = num%10
    result = (result*10)+rem
    num //= 10
    
if result == number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")