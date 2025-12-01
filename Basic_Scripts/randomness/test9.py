def add(x,y):
    return x + y
def susb(x,y):
    return x - y 
def multiply(x,y):
    return x * y
def divis(x,y):
    if y == 0:
        return "can't divide on 0"
    return x / y

def number():
    a = int(input("enter the first number"))
    b = int(input("enter the seconde number"))
    return a,b

def proc():
    process = input("enter the proccess you want to use '+,-,*,/'")
    return process

def main():
    num1, num2 = number()
    process = proc()

    if process == '+':
        result = add(num1,num2)
    elif process == '-':
        result = susb(num1,num2)
    elif process == '*':
        result = multiply(num1,num2)
    elif process == '/':
        result = divis(num1,num2)
    else:
        print("please enter one of those proccess")
        return
    print("Result is: ",result)

main()

