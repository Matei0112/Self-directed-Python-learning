#conditional expressions

num=6
a=6
b=7
age=25
temp=19
user_role="admin"


#print("positive" if num>0 else "Negative")

#result= "even"if num%2==0 else "odd"

#max_num= a if a>b else b
#min_num= a if b>a else b
#status="adult" if age>=18 else "Child"

#weather="hot" if temp>20 else "cold"

access_level="admin" if user_role=="admin" else "Access denied"

print(access_level)