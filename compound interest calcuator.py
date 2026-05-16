#compound interest calculator

Cash = float(input("Please enter your start cash amount: "))
compound = float(input("Enter compound interest rate: 0.01-0.99 "))
Years = int(input("Enter number of years on interest: "))
Total = Cash * (compound + 1)**Years

if Cash < 0:
    print("You have no money, please come back when you have more")
if compound < 0:
    print("You can not have negative interest, please choose a higher value")

print(f"your total earnings with compound interest is ${round(Total, 2)}")