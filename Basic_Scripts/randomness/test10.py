def get_number():
    x = int(input("enter the number you want to check"))
    return x

def get_divis(x):
    if x % 2 == 0:
        print("your number is even")
    elif x % 2 != 0:
        print("your number is odd")

def main():
    num1 = get_number()
    result = get_divis(num1)
    print(result)

main()

