#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3 username must not contain digits

username= input("Enter your username: ")



if len(username)>12:
    print("Your username is too long")
elif not username.isalpha():
    print("Your username Can not contain any digits")
elif not username.find(" ")== -1:
    print("Your username must not contain spaces")
else:
    print(f"{username} Welcome to our website")


