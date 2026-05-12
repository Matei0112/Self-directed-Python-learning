import math
from math import ceil
#calculating the circumfrence of a circle

radius = float(input("Enter radius: "))

circumference = 2*math.pi*radius

print(f"The Circumference is: {circumference}")


#lets calculate area of a circle

area = math.pi*pow(radius,2)

print(f"The area is {round(area)} cm**2")