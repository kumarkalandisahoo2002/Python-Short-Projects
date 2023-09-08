#calculate the sum of all the digits in a given number

number = int(input("Enter a number:\n"))
num = number

sum = 0
while num != 0:
    rem = num%10
    sum += rem
    num //= 10

print(f"The sum of all the digits in {number} is: ",sum)