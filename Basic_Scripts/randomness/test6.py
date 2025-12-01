def check_password(uinput):
    return uinput == 'python'

uinput = input("enter the password: ")

while not check_password(uinput):
    uinput = input("Wrong password, try again: ")

print("congrats. you got the password")
