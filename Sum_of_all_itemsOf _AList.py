'''sum of all the items in a list'''

# #Method :- #1
# lst = [12,8,50,60,40,30,40,60]
# print(len(lst))
# i = 0
# sum_ = 0
# while (i < len(lst)):
#      sum_ += lst[i]
#      i += 1
# print("The sum of all the items in the list is :: ",sum_)


#Method :- #2
# def sumitems(list):
#     i = 0; sum_ = 0
#     while i < len(list):
#         sum_ += list[i]
#         i += 1
#     return sum_

# lst = [12,8,50,60,40,30,40,60]
# print("The sum of all the items in the list is :: ",sumitems(lst))
    
'''Doubt'''   
#Method :- #3
def sumitems(list):
    i = 0; sum_ = 0
    while i < len(list):
        sum_ += list[i]
        i += 1
    return sum_

lst = []
print("Enter a list having 5 items::")
for i in range(5):
    x = int(input("Enter item : "))
    lst = lst.append(x)
    
print(lst)
print("The sum of all the items in the list is :: ",sumitems(lst))