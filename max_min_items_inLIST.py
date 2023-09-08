'''finding smallest items in a list'''

"""using user-defined function & user input method"""
list_ = []
num = int(input("Enter the number of items in the list: "))
for i in range(num):
    element = int(input("Enter the element:: "))
    list_.append(element)

print("The smallest items in the list is:: ",min(list_))
print("The largest items in the list is:: ",max(list_))



"""using hard coded value"""

# lst1 = [12,34,23,45,35,67,68]
# lst2 = lst1.copy()
# lst1.sort(reverse=True)     #descending order
# lst2.sort()     #assending order

# """using sort() method"""
# print("The smallest number in the list is:: ",lst1[-1])
# print("The largest number in the list is:: ",lst2[-1])

# """using min() & max() method"""
# lst3 = [12,34,23,45,35,67,68]
# print("The smallest number in the list is:: ",min(lst3))
# print("The largest number in the list is:: ",max(lst3))




