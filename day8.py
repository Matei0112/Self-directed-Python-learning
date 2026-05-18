unit = input("Is this temperature in celsius or fahrenheit (C/F): ")
temp=float(input("Enter the temperature "))
if unit == "C":
    temp=round((temp*9)/5+32, 1)
    print("The temperature in fahrenheit is " + str(temp) )

elif unit == "F":
    temp=round((temp-32)*5/9, 1)
    print("The temperature in celsius is " + str(temp) )
else:print(f"{unit} is invalid ")





