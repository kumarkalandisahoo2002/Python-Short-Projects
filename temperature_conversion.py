""""Temperature convertor"""
m1 = input("Choose a temperature mode(C,K or F) : ")
m2 = input("Choose a temperature mode in which you convert your temperature(C,K or F) : ")

if m1 == "C" and m2 == "K":
    print("Conversion from Celcius to Kelvin:")
    temp1 = float(input("Enter the temperature in celcius: "))
    temp2 = 273.15 + temp1
    print("Corresponding temperature in Kelvin is: ",temp2)

if m1 == "K" and m2 == "C":
    print("Conversion from Kelvin to Celcius:")
    temp1 = float(input("Enter the temperature in kelvin: "))
    temp2 = temp1 - 273.15
    print("Corresponding temperature in Celcius is: ",temp2)
    
if m1 == "F" and m2 == "C":
    print("Conversion from Farenheit to Celcius:")
    temp1 = float(input("Enter the temperature in Farenheit : "))
    temp2 = (temp1 - 32) * (5/9)
    print("Corresponding temperature in Celcius is: ",temp2)
    
if m1 == "C" and m2 == "F":
    print("Conversion from Celcius to Fahenheit:")
    temp1 = float(input("Enter the temperature in Celcius : "))
    temp2 = (temp1*(9/5)) + 32
    print("Corresponding temperature in Farenheit is: ",temp2)
    
if m1 == "K" and m2 == "F":
    print("Conversion from Kelvin to Fahenheit:")
    temp1 = float(input("Enter the temperature in Kelvin : "))
    temp2 = (temp1 - 273.15)*(9/5) + 32
    print("Corresponding temperature in Farenheit is: ",temp2)
    
if m1 == "F" and m2 == "K":
    print("Conversion from Fahenheit to Kelvin:")
    temp1 = float(input("Enter the temperature in Farenheit : "))
    temp2 = (temp1 - 32)*(5/9) + 273.15
    print("Corresponding temperature in Kelvin is: ",temp2)