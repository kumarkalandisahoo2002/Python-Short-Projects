mark01 = int(input("Enter first mark:\n"))
mark02 = int(input("Enter second mark:\n"))
mark03 = int(input("Enter third mark:\n"))

Total = mark01 + mark02 + mark03
percentage = (Total/300)*100
print(percentage)
print()
if percentage >= 40:
    if mark01 >= 33 and mark02 >= 33 and mark03 >= 33:
        print("You are passed as you got 33 percentage above in all individual subjects")
    else:
        print("Sorry! You are failed as you not got 33 percentage above in all individual subjects")
else:
    print("Sorry! You are failed as you not got above 40 percentage")