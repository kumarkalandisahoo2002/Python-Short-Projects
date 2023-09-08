#reverse a given number

number = int(input("Enter a number:\n"))
num = number
result = 0
while num != 0:
    rem = num%10
    result = (result*10)+rem
    num //= 10
    
print(f"The reverse of {number} is: ",result)