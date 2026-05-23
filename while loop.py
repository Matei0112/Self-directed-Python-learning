#while loop= execute some code while some condition remains true

num=int(input("Enter a number: "))

while num<1 or num>10:
    print(f"Variable {num} is not valid")
    num=int(input("Enter a number: "))

print(f"The number is {num}")