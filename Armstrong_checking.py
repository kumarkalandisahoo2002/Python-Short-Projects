#checking a number is armstrong or not
number = int(input("Enter a number:\n"))
num = number

i = 0
while num != 0:
    i += 1
    num //= 10

num = number
sum = 0
for n in range(i): #or range(0,i,1):
    result = 1
    rem = num%10
    result *= rem**i
    sum += result
    num //= 10

if sum == number:
    print(f"The number {number} is a Armstrong number.")
else:
    print(f"The number {number} is not a Armstrong number.")

