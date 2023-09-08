"""                                                       Using if...elif...else ladder                                               """

# #accessing & printing current time
# import time
# TimeStamp = time.strftime("%H:%M:%S")   #it is a string
# print(f"Current Time is {TimeStamp}")
# Hour = int(time.strftime('%H')) #it is a string
# print()

# """Greeting"""
# if 5 < Hour <= 11:
#     print("Good Morning, sir.") 
# elif 11 < Hour <= 16:
#     print("Good afternoon, sir.")
# elif 16 < Hour <= 19:
#     print("Good evening, sir.")
# else:
#     print("Good night, sir.")


"""                                                       Using match case statement                                                 """

import time
TimeStamp = time.strftime('%H:%M:%S')
print(f"Current Time is {TimeStamp}")

Hour = int(time.strftime("%H"))

match Hour:
    case _ if 5 < Hour <= 11:       #for default case use "_" or you can give value as in switch case value.
        print("Good Morning, sir.")
    case _ if 11 < Hour <= 16:
        print("Good afternoon, sir.")
    case _ if 16 < Hour <= 19:
        print("Good evening, sir.")
    case _:
        print("Good night, sir.")
    
    