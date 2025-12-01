def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Can't devide on 0"
    return x / y

def get_numbers():
    a = int(input("enter the first number: "))
    b = int(input("enter the seconde number: "))
    return a, b

def get_proc():
    return input("Enter one of the process (+,-,*,/)")

def main():
    n1, n2 = get_numbers()
    proc = get_proc()

    if proc == '+':
        result = add(n1,n2)
    elif proc == '-':
        result = substract(n1,n2)
    elif proc == '/':
        result = divide(n1,n2)
    elif proc == '*':
        result = multiply(n1,n2)
    else:
        result = "Invalid operation choose wisely"

    print("Result:", result)

main()
