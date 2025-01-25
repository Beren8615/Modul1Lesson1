import random
password = ""
characters = "ABCDEFGHIJKLMNOPRSTUVYZabcdefghijklmnoprstuvyz0123456789!'^+%&/()=?_*/>|"
password_length = int(input("How many characters should a password be?"))
if password_length == 0:
    print("Try again!!!")
else:
    for i in range(password_length):
        password += random.choice(characters)
print("Are you sure?")
input("")
print("You are welcome!")
print(password)
