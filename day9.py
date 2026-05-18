#logical operators, boolean operators, or=at least one is true, and= both must be true, not=flips the condition

temp = 20
is_sunny=True
if temp >= 25 and is_sunny:
    print("ITSS SHINING OUTSIDE")
elif temp <= 0 and is_sunny:
    print("ITSS FREEEZING OUTSIDE")
elif 25 > temp > 0 and is_sunny:
    print("ITSS SHINING OUTSIDE")