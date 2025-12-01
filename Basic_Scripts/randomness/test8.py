import random

def game():
    number = random.randint(1,9999)
    tries = 0

    while True:
        guess = int(input("enter the secret number"))
        tries +=1

        if guess == number:
             print("you got the hidden number the number is",{number},"and you got it in",{tries},"tries. Congrats")
             break
        elif guess > number:
            print("you are too high")
        else:
            print("you are too low")


