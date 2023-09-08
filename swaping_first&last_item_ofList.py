'''Interchange first & last element in a list'''
def swapitem(list):
    list[0],list[-1] = list[-1],list[0]
    print("updated list :: ",list)

list_old = [12,4,34,65,67,45,67,40]
print("old list is:\t",list_old)
print(swapitem(list_old))
