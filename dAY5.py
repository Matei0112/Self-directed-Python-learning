#if statements, only if some condition is true, else we can do something else

age=int(input("enter your age"))

if age>=100:
    print("you are a too old to sign up")
if age>=18:
    print("you are now signed up")
elif age<0:
    print("you haven't been born yet")

else:
    print("you must be 18+ to sign up")

for_sale= False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")