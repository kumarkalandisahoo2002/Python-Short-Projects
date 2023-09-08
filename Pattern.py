"""                                                by using while_loop                                                                  """
                                                
#decreasing star pattern
    #taking input method
i = input("Enter the row number:: ")
n = 1
while int(i) >= n:
    print(int(i) * "* ")
    i = int(i) - 1

    
#increasing star pattern
    #taking input metod
j = input("Enter the row number:: ")
n = 1
while n <= int(j):
    print(n * "* ")
    n = n + 1

        #another method
#decreasing star pattern
"""
i = 5
while i >= 1:
    print(i * "*")
    i = i - 1
"""
#increasing star pattern  
"""
i = 1
while i <= 5:
    print(i * "*")
    i += 1
"""

print()
print()


"""                                              by using for_loop                                                                     """

r1 = input("Enter the row number:: ")
for i in range(1,int(r1 ) + 1,1):
    print(i * "* ")

print()

r2 = input("Enter the row number:: ")
for j in range(int(r2),0,-1):
    print(j * "* ")



