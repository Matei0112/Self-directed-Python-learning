#format specifers =[value:flags} format a value based on what flags are inserted


price1=3000.14159
price2=-10000.65
price3=12000.34

print(f"price1  is ${price1:<,.2f}")
print(f"price2  is ${price2:+,.2f}")
print(f"price3  is ${price3:+,.2f}")